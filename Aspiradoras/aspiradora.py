from mesa import Agent
from basura import Basura


class Aspiradora(Agent):
    def __init__(self, unique_id, model):
        super().__init__(model)
        self.unique_id = unique_id

    def step(self):
        contenido_celda = self.model.grid.get_cell_list_contents([self.pos])
        basura_aqui = [obj for obj in contenido_celda if isinstance(obj, Basura)]

        if len(basura_aqui) > 0:
            basura = basura_aqui[0]
            self.model.grid.remove_agent(basura)
            self.model.agents.remove(basura)
        else:
            vecinos = self.model.grid.get_neighborhood(self.pos, True, False)
            vecinos_validos = []

            for vecino in vecinos:
                contenido_vecino = self.model.grid.get_cell_list_contents([vecino])
                hay_aspiradora = any(isinstance(obj, Aspiradora) for obj in contenido_vecino)

                if not hay_aspiradora or vecino == (1, 1):
                    vecinos_validos.append(vecino)

            if len(vecinos_validos) > 0:
                nueva_posicion = self.random.choice(vecinos_validos)
                self.model.grid.move_agent(self, nueva_posicion)