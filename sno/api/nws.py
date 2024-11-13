'''
Wrapper around the NOAA weather forecasting api.
'''
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Iterable, List

import requests


@dataclass
class GridPoint:
    forecast_office: str
    x: int
    y: int


@dataclass
class TextProduct:
    id: str
    timestamp: datetime
    office: str
    code: str
    name: str

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> 'TextProduct':
        return cls(
            id=data["id"],
            timestamp=datetime.fromisoformat(data["issuanceTime"]),
            office=data["issuingOffice"],
            code=data["productCode"],
            name=data["productName"],
        )


class WeatherApi:
    base_url: str = "https://api.weather.gov"
    session_headers: Dict[str, str] = {
        "User-Agent": "(sno app, contact: camderwin@gmail.com)",
        "Accept": "geo+json",
    }

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(**self.session_headers)

    def get_forecast(self, grid_point: GridPoint) -> Any:
        response = self.session.get(f"{self.base_url}/gridpoints/{grid_point.forecast_office}/{grid_point.x},{grid_point.y}")
        response.raise_for_status()
        return response.json()

    def get_textual_forecast(self, grid_point: GridPoint) -> Any:
        response = self.session.get(f"{self.base_url}/gridpoints/{grid_point.forecast_office}/{grid_point.x},{grid_point.y}/forecast")
        response.raise_for_status()
        return response.json()
    
    def get_hourly_forecast(self, grid_point: GridPoint) -> Any:
        response = self.session.get(f"{self.base_url}/gridpoints/{grid_point.forecast_office}/{grid_point.x},{grid_point.y}/forecast/hourly")
        response.raise_for_status()
        return response.json()

    def coordinate_to_gridpoint(self, latitude: float, longitude: float) -> GridPoint:
        response = self.session.get(f"{self.base_url}/points/{latitude},{longitude}")
        response.raise_for_status()
        props = response.json()["properties"]
        return GridPoint(forecast_office=props["gridId"], x=props["gridX"], y=props["gridY"])

    def list_products(self, product_type: str, product_location: str) -> List[TextProduct]:
        response = self.session.get(f"{self.base_url}/products/types/{product_type}/locations/{product_location}")
        response.raise_for_status()
        return [TextProduct.from_json(data) for data in response.json()["@graph"]]

    def fetch_product_text(self, product: TextProduct) -> str:
        response = self.session.get(f"{self.base_url}/products/{product.id}")
        response.raise_for_status()
        return response.json()["productText"]
