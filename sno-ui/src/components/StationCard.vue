<script setup>
defineProps(['title'])
</script>

<template>
  <div class="card">
    <div class="card-header">
      <h3 class="card-title">{{ title }}</h3>
    </div>
    <div class="card-body"></div>
  </div>
</template>

<style>
.card-body {
  min-height: 10rem;
}
</style>
