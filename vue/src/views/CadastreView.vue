<script setup lang="ts">
import { useApi } from "@/services/api";
import { ref } from "vue";
import type { Entidade } from "@/services/api";

const api = useApi();

const entidade = ref<Entidade>({
  nome: "",
  cnpj: "",
  rua: "",
  bairro: "",
  cidade: "",
  cep: "",
  sobre: "",
});

const onSubmit = async () => {
  await api.entidades.createEntidade(entidade.value);
};
</script>

<template>
  <main class="px-3">
    <div class="col-md-6 offset-md-3">
      <h1>CADASTRE A SUA ENTIDADE</h1>
      <p class="lead">
        Para se cadastrar é fácil, insira as informações a baixo:
      </p>
    </div>
  </main>
  <div class="col-md-4 offset-md-3">
    <form method="POST" @submit.prevent="onSubmit">
      <h4>Dados</h4>

      <div class="form-group">
        <label for="nomeInput">Nome</label>
        <input
          v-model="entidade.nome"
          type="text"
          class="form-control"
          id="nameInput"
          placeholder="Nome da Entidade"
        />
      </div>

      <div class="form-group">
        <label for="cnpjInput" class="text-secondary">CNPJ </label>
        <input
          v-model="entidade.cnpj"
          type="text"
          class="form-control"
          id="cnpjInput"
          placeholder="CNPJ"
        />
      </div>

      <div class="form-group">
        <label for="sobreInput">Sobre</label>
        <textarea
          v-model="entidade.sobre"
          class="form-control"
          id="sobreInput"
          rows="3"
          placeholder="Conte um pouco sobre o trabalho que é realizado"
        />
      </div>

      <div class="row mt-3">
        <h4>Endereço</h4>

        <div class="form-group">
          <label for="ruaInput">Rua</label>
          <input
            v-model="entidade.rua"
            type="text"
            class="form-control"
            id="ruaInput"
            placeholder="rua exemplo, n 123"
          />
        </div>

        <div class="form-group">
          <label for="bairroInput">Bairro</label>
          <input
            v-model="entidade.bairro"
            type="text"
            class="form-control"
            id="bairroInput"
            placeholder="Bairro exemplo"
          />
        </div>

        <div class="form-group">
          <label for="cidadeInput">Cidade</label>
          <input
            v-model="entidade.cidade"
            type="text"
            class="form-control"
            id="cidadeInput"
            placeholder="Qual a cidade?"
          />
        </div>

        <div class="form-group">
          <label for="cepInput">CEP</label>
          <input
            v-model="entidade.cep"
            type="text"
            class="form-control"
            id="cepInput"
            placeholder="Informe o CEP"
          />
        </div>
      </div>

      <p></p>
      <button type="submit" class="btn btn-primary">Cadastrar</button>
    </form>
  </div>
</template>
