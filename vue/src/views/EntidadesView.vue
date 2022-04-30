<script setup lang="ts">
import { onMounted, ref } from "vue";
import type { Entidade } from "@/services/api";
import { useApi } from "@/services/api";

const api = useApi();

const entidades = ref<Entidade[]>([]);

onMounted(async () => {
  entidades.value = (await api.entidades.getEntidades()).entidades;
});
</script>

<template>
  <main class="px-3">
    <div class="col-md-12 offset-md-3">
      <h1 class="display-5">ENTIDADES CADASTRADAS</h1>
      <p class="lead"></p>
    </div>
  </main>

  <div class="p-5"></div>

  <div v-for="entidade in entidades" :key="entidade.nome">
    <div class="p-2 mb-3 bg-dark rounded-3">
      <div class="container-fluid py-1">
        <h5 class="display-7 fw-bold text-light">{{ entidade.nome }}</h5>
        <p class="col-md-8 fs-6 text-light">
          Endereço: {{ entidade.rua }}, {{ entidade.bairro }},
          {{ entidade.cidade }}
        </p>
        <p class="col-md-8 fs-6 text-light">E-mail: {{ entidade.email }}</p>
        <p class="col-md-8 fs-6 text-light">Sobre: {{ entidade.sobre }}</p>
      </div>
    </div>
  </div>
</template>
