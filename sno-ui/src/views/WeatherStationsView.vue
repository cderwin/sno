<script setup>
import StationCard from '@/components/StationCard.vue'
import sourceData from '../data.json'

const stationData = sourceData.stations
</script>

<template>
  <div class="station-card-container">
    <StationCard v-for="station in stationData" :key="station.id" :title="station.name" />
  </div>
</template>

<style>
.station-card-container {
  display: grid;
  gap: 2rem;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-columns: 1fr;

  padding-block: 2rem;
  width: min(95%, 70rem);
  margin-inline: auto;
}
</style>
