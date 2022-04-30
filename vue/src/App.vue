<script setup lang="ts">
import { RouterView } from "vue-router";
</script>

<template>
  <main>
    <div class="container py-4">
      <header class="pb-3 mb-4 border-bottom">
        <a
          href="/"
          class="d-flex align-items-center text-dark text-decoration-none"
        >
          <span class="fs-2">PRODEA</span>
        </a>
      </header>
      <RouterView />
    </div>
  </main>
</template>
