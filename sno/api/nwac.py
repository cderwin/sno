'''
Wrapper of the api used to access nwac telemetry.
'''

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional

import numpy as np
import requests

snowobs_api_url = "https://api.snowobs.com/wx/v1/station/data/timeseries/"
nwac_api_token = "71ad26d7aaf410e39efe91bd414d32e1db5d"  # this is public, pulled from nwac client-side js
date_format = "%Y%m%d%H%M"
default_params = {
    "token": nwac_api_token,
    "source": "nwac",
}

global_station_ids: Dict[str, List[int]] = {
    "Alpental": [1, 2, 3],
    "Hurricane Ridge": [4],
    "Mt. Baker Ski Area": [5, 6],
    "Mazama": [7],
    "Washington Pass": [8, 9],
    "Dirtyface Summit": [10],
    "Lake Wenatchee": [11],
    "Berne": [12],
    "Stevens Pass": [13, 14, 17, 18, 50, 51],
    "Tumwater Mountain": [19],
    "Mt. Washington": [20],
    "Snoqualmie Pass": [21, 22, 23],
    "Mission Ridge": [24, 25, 26],
    "Crystal": [27, 28, 29, 54],
    "Sunrise": [30, 31],
    "Chinook Pass": [32, 33],
    "Camp Muir": [34],
    "Paradise": [35, 36],
    "White Pass": [37, 39, 49],
    "Mt. St. Helens": [40],
    "Mt. Hood Meadows": [41, 42, 43],
    "Timberline": [44, 45, 56],
    "Skibowl": [46, 47],
    "Blewett Pass": [48],
    "Leavenworth": [53],
    "White Chuck Mountain": [57],
}


@dataclass
class StationMetadata:
    uuid: str
    station_id: int
    station_name: str
    latitude: float
    longitude: float
    altitude: float

    @classmethod
    def from_response_data(cls, station_data: Dict[str, Any]) -> "StationMetadata":
        return cls(
            uuid=station_data["id"],
            station_id=station_data["stid"],
            station_name=station_data["name"],
            latitude=station_data["latitude"],
            longitude=station_data["longitude"],
            altitude=station_data["elevation"],
        )


@dataclass
class Station:
    metadata: StationMetadata
    timestamps: np.ndarray
    observations: Dict[str, np.ndarray]

    @classmethod
    def from_response_data(cls, stations_data: List[Dict[str, Any]]) -> "List[Station]":
        stations = []
        for station_data in stations_data:
            observations_data = station_data.pop("observations")
            timestamps_data = observations_data.pop("date_time")
            timestamps = np.array(
                [datetime.fromisoformat(ts) for ts in timestamps_data]
            )
            observations = {
                short_name: np.array(values)
                for short_name, values in observations_data.items()
            }
            stations.append(cls(
                metadata=StationMetadata.from_response_data(station_data),
                timestamps=timestamps,
                observations=observations,
            ))
        
        return stations


@dataclass
class PropertyMetadata:
    short_name: str
    long_name: str
    units: str

    @classmethod
    def from_response_data(
        cls, units_data: Dict[str, str], variables_data: List[Dict[str, str]]
    ) -> "List[PropertyMetadata]":
        return [
            cls(
                short_name=variable["variable"],
                long_name=variable["long_name"],
                units=units_data[variable["variable"]],
            )
            for variable in variables_data
        ]


class Location:
    name: str
    _fetched: bool = False
    _stations: Optional[Dict[int, Station]] = None
    _properties: Optional[List[PropertyMetadata]] = None

    def __init__(self, name: str):
        if name not in global_station_ids.keys():
            raise ValueError("invalid station name")
        self.name = name

    @property
    def stations(self) -> List[Station]:
        if not self._fetched:
            self.fetch()

        return self._stations

    @property
    def properties(self) -> List[PropertyMetadata]:
        if not self._fetched:
            self.fetch()

        return self._properties

    @property
    def dataframe(self) -> "pd.DataFrame":
        try:
            import pandas as pd
        except ImportError:
            raise RuntimeError("Could not import pandas; try installing")

        raise NotImplementedError

    def fetch(self) -> None:
        station_ids = global_station_ids[self.name]
        response_data = self.fetch_data(station_ids)

        self._properties = PropertyMetadata.from_response_data(
            response_data["UNITS"], response_data["VARIABLES"]
        )
        self._stations = {
            station.metadata.station_id: station
            for station in Station.from_response_data(response_data["STATION"])
        }
        self._fetched = True

    @staticmethod
    def fetch_data(
        station_ids: List[int],
        start: Optional[datetime] = None,
        end: Optional[datetime] = None,
    ) -> Dict[str, Any]:
        if start is None and end is None:
            end = datetime.now(timezone.utc)
            start = end - timedelta(days=1)
        elif start is None:
            start = end - timedelta(days=1)
        elif end is None:
            end = start + timedelta(days=1)

        params = default_params.copy()
        params["stid"] = station_ids
        params["start_date"] = start.strftime(date_format)
        params["end_date"] = end.strftime(date_format)
        response = requests.get(snowobs_api_url, params=params)
        response.raise_for_status()
        return response.json()
