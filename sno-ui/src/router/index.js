import { createRouter, createWebHistory } from 'vue-router'
import WeatherStationsView from '../views/WeatherStationsView.vue'
import ForecastsView from '../views/ForecastsView.vue'
import MappingView from '../views/MappingView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/', name: 'home', redirect: '/observations'},
    {path: '/observations', name: 'weather_stations', component: WeatherStationsView},
    {path: '/forecasts', name: 'forecasts', component: ForecastsView},
    {path: '/maps', name: 'mapping', component: MappingView},
  ],
  linkActiveClass: "active"
})

export default router
