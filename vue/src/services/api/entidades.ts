import axios from "axios";
import type { Entidade } from "./types";

export const entidades = {
  /**
   * Faz uma requisição à API e retorna as entidades cadastrados.
   *
   * @param {Partial<Entidade>|null} filtro Filtro de busca.
   * Os atributos devem possuir os nomes dos atributos da entidade.
   * @returns {Promise<{entidades: Entidade[]}>} Resposta da API.
   */
  getEntidades: (
    filtro: Partial<Entidade> = {}
  ): Promise<{ entidades: Entidade[] }> =>
    axios
      .get("/api/entidades", { params: filtro })
      .then((response) => response.data),

  /**
   * Faz uma requisição à API e retorna uma entidade cadastrada referente ao "email" informado.
   *
   * @param {string} email Email da entidade.
   * @returns {Promise<{entidade:Entidade}>} Resposta da API.
   */
  getEntidade: (email: string): Promise<{ entidade: Entidade }> =>
    axios.get(`/api/entidade/${email}`).then((response) => response.data),

  /**
   * Faz uma requisição à API para criar uma nova entidade.
   *
   * @param {Entidade} entidade Dados da entidade que será criada.
   * @returns {Promise<{entidade:Entidade}>} Resposta da API.
   */
  createEntidade: (entidade: Entidade): Promise<{ entidade: Entidade }> =>
    axios.post("/api/entidades", entidade).then((response) => response.data),

  /**
   * Faz uma requisição à API para alterar uma entidade.
   *
   * @param {Entidade} entidade Dados da entidade que será criada.
   * @returns {Promise<{entidade: Entidade}>} Resposta da API.
   */
  updateEntidade: (entidade: Entidade): Promise<{ entidade: Entidade }> =>
    axios
      .patch(`/api/entidades/${entidade.email}`, entidade)
      .then((response) => response.data),

  /**
   * Faz uma requisição à API para excluir uma entidade.
   *
   * @param {string} email Email da entidade.
   * @returns {Promise<{}>} Resposta da API.
   */
  deleteEntidade: (email: string): Promise<object> =>
    axios.delete(`/api/entidades/${email}`).then((response) => response.data),
};
