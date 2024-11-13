<script setup>
import { RouterLink, RouterView } from 'vue-router'
import IconHeart from './components/icons/IconHeart.vue'
import IconSnowflake from './components/icons/IconSnowflake.vue'
</script>

<template>
  <header class="navbar navbar-expand-sm navbar-light d-print-none">
    <div class="container-xl">
      <h1 class="navbar-brand navbar-brand-autodark d-none-navbar-horizontal pe-0 pe-md-3">
        <router-link :to="{ name: 'home' }"><IconSnowflake /> sno</router-link>
      </h1>

      <div class="d-flex collapse navbar-collapse justify-content-center" id="navbarText">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'weather_stations' }"
              >Weather Stations</router-link
            >
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'forecasts' }">Forecasts</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'mapping' }">Mapping</router-link>
          </li>
        </ul>
      </div>
      <div class="justify-content-right">
        <span class="navbar-text">
          made w <IconHeart /> by <a href="https://cderwin.github.io/">cameron</a>
        </span>
      </div>
    </div>
  </header>

  <div class="container-xl"><RouterView /></div>
</template>

<style>
:root {
  --cd-navbar-border-width: 1px;
  --cd-navbar-border-color: #e6e7e9;
}

.cd-navbar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;

  position: relative;
  padding: 0.25rem 0rem;
  min-height: 3.5rem;

  color: #1d273b;
  background: #ffffff;
  box-shadow: inset 0 calc(-1 * var(--cd-navbar-border-width)) 0 0 var(--cd-navbar-border-color);
}

@media (min-width: 576px) {
  .cd-navbar {
    flex-wrap: nowrap;
    justify-content: space-between;
  }
}

.nav-item .active {
  /* border-bottom: 3px solid hsla(202, 79%, 30%, 0.89); */
  border-bottom: 3px solid var(--color-text);
}

.navbar a {
  text-decoration: none;
  color: var(--color-text);
  transition: 0.4s;
  padding: 3px;
}

@media (hover: hover) {
  .navbar a:hover {
    background-color: hsla(202, 71%, 48%, 0.2);
  }
}
</style>
