import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CadastreView from "../views/CadastreView.vue";
import CadastroConcluidoView from "../views/CadastroConcluidoView.vue";
import ProdeaView from "../views/ProdeaView.vue";
import EntidadesView from "../views/EntidadesView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/cadastre",
      name: "cadastre",
      component: CadastreView,
    },
    {
      path: "/cadastro-concuido",
      name: "cadastro-concuido",
      component: CadastroConcluidoView,
    },
    {
      path: "/prodea",
      name: "prodea",
      component: ProdeaView,
    },
    {
      path: "/entidades",
      name: "entidades",
      component: EntidadesView,
    },
  ],
});

export default router;
