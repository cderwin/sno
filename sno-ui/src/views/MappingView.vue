<template>
  <div class="map-controls">
    <button @click="resize_map" class="btn btn-outline-primary">Resize map</button>
  </div>
  <div class="map-container">
    <div id="map"></div>
  </div>
</template>

<script setup>
import sourceData from '../data.json'
import mapboxgl from 'mapbox-gl'
import { onMounted } from 'vue'

let map = null

onMounted(() => {
  if (!map) {
    mapboxgl.accessToken = sourceData.mapbox.api_key
    map = new mapboxgl.Map({
      container: 'map',
      center: [-122.3328, 47.6061],
      style: sourceData.mapbox.map_style,
      zoom: 9,
      attributionControl: false,
    })
    map.on('load', () => {
      map.resize()
    })
  }
})

function resize_map(event) {
  map.resize()
}
</script>

<style>
.map-controls {
  padding: 20px 10px;
}

.map-container {
  display: flex;
  flex-flow: column;
  height: 75vh;
  margin: 10px 0px 50px 0px;
}

#map {
  height: 100%;
  margin-bottom: 50px;
}
</style>
