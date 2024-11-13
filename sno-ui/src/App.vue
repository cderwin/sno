<script setup>
import { RouterLink, RouterView } from 'vue-router'
import IconHeart from './components/icons/IconHeart.vue'
import IconSnowflake from './components/icons/IconSnowflake.vue'
</script>

<template>
  <header class="cd-navbar">
    <span class="cd-navbar-logo">
      <router-link :to="{ name: 'home' }"><IconSnowflake /> sno</router-link>
    </span>

    <ul class="cd-navbar-routes">
      <li>
        <router-link class="nav-link" :to="{ name: 'weather_stations' }">
          Weather Stations
        </router-link>
      </li>
      <li>
        <router-link class="nav-link" :to="{ name: 'forecasts' }">Forecasts</router-link>
      </li>
      <li>
        <router-link class="nav-link" :to="{ name: 'mapping' }">Mapping</router-link>
      </li>
    </ul>

    <span class="cd-navbar-attribution">
      made w <IconHeart /> by <a href="https://cderwin.github.io/">cameron</a>
    </span>
  </header>

  <div class="content"><RouterView /></div>
</template>

<style>
:root {
  --cd-navbar-responsive-size: 600px;
  --cd-navbar-border-width: 1px;
  --cd-navbar-border-color: #e6e7e9;
}

.cd-navbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;

  position: relative;
  padding: 0.25rem 5rem;
  min-height: 3.5rem;

  color: #1d273b;
  background: #ffffff;
  box-shadow: inset 0 calc(-1 * var(--cd-navbar-border-width)) 0 0 var(--cd-navbar-border-color);
}

@media (min-width: 600px) {
  .cd-navbar {
    flex-wrap: nowrap;
    justify-content: space-between;
  }
}

.cd-navbar-routes {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 2rem;

  list-style: none;
  margin-bottom: 0rem;

  & a {
    padding: 0.5rem 1rem;
    border-radius: 5%;
  }
}

@media (min-width: 600px) {
  .cd-navbar-routes {
    flex-wrap: nowrap;
    justify-content: center;
    gap: 2rem;
  }
}

.cd-navbar-logo {
  a,
  a:hover,
  a:focus {
    color: #247ba0;
    text-decoration: none;
  }
}

.cd-navbar-attribution {
  padding: 0.5rem 1rem;

  a,
  a:hover,
  a:focus {
    color: #247ba0;
  }
}

.active {
  border-bottom: 3px solid var(--color-text);
}

@media (hover: hover) {
  .cd-navbar-routes a:hover {
    background-color: hsla(202, 71%, 48%, 0.2);
  }
}

.content {
  width: 100%;
  padding-left: 0.625rem;
  padding-right: 0.625rem;
  margin-left: auto;
  margin-right: auto;
}

@media (min-width: 1200px) {
  .content {
    max-width: 1140px;
  }
}

@media (min-width: 1400px) {
  .content {
    max-width: 1320px;
  }
}
</style>
