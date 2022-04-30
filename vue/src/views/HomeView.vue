<script setup lang="ts"></script>

<template>
  <div class="p-5 mb-4 bg-dark rounded-3">
    <div class="container-fluid py-5">
      <h1 class="display-5 fw-bold text-white">
        PROGRAMA DE DOAÇÃO DE ALIMENTOS
      </h1>
      <p class="col-md-8 fs-4 text-white">
        O prodea é um programa que se baseia na Lei Nº 14016, de 23 de Junho de
        2020, e tem como objetivo facilitar a doação de alimentos a entidades
        beneficentes.
      </p>
      <router-link class="btn btn-light btn-lg" to="cadastre" role="button">
        Cadastre uma entidade
      </router-link>
      <router-link class="btn btn-light btn-lg" to="entidades" role="button">
        Entidades participantes
      </router-link>
    </div>
  </div>

  <div class="row align-items-md-stretch">
    <div class="col-md-6">
      <div class="h-100 p-5 text-black bg-light rounded-3">
        <h2>Conheça a lei</h2>
        <p>Ainda não conhece a lei Nº 14016?</p>
        <a
          class="btn btn-outline-secondary"
          href="https://www.in.gov.br/web/dou/-/lei-n-14.016-de-23-de-junho-de-2020-263187111"
          target="_blank"
          role="button"
        >
          Saiba mais
        </a>
      </div>
    </div>
    <div class="col-md-6">
      <div class="h-100 p-5 bg-light border rounded-3">
        <h2>Conheça o projeto</h2>
        <p>O que é o PRODEA?</p>
        <router-link
          class="btn btn-outline-secondary"
          to="prodea"
          role="button"
        >
          saiba mais
        </router-link>
      </div>
    </div>
  </div>

  <footer class="pt-3 mt-4 text-muted border-top">&copy; 2021</footer>
</template>
