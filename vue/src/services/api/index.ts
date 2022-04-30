import { entidades } from "./entidades";
import type { Entidade } from "./types";

export type { Entidade };

export const useApi = () => {
  return { entidades };
};
