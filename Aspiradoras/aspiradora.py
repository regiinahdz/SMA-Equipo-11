# Programa: implementa el comportamiento de un agente aspirador.
# Autores: Regina Hernández Moreno - A01802688; Ricardo Oved Cornejo Castro - A01803272
# Fecha de creacion/modificacion: 16/11/2026

from mesa import Agent
from basura import Basura


class Aspiradora(Agent):
    # Inicializa el agente aspirador.
    # Parametros: self, instancia actual; uniqueId, identificador solicitado; model, modelo al que pertenece.
    # Retorno: None.
    def __init__(self, uniqueId, model):
        super().__init__(model)
        self.uniqueId = uniqueId

    # Limpia la celda actual o mueve la aspiradora a una celda vecina disponible.
    # Parametros: self, instancia actual.
    # Retorno: None.
    def step(self):
        contenidoCelda = self.model.grid.get_cell_list_contents([self.pos])
        basuraAqui = [obj for obj in contenidoCelda if isinstance(obj, Basura)]

        if len(basuraAqui) > 0:
            basura = basuraAqui[0]
            self.model.grid.remove_agent(basura)
            self.model.agents.remove(basura)
        else:
            vecinos = self.model.grid.get_neighborhood(self.pos, True, False)
            vecinosValidos = []

            for vecino in vecinos:
                contenidoVecino = self.model.grid.get_cell_list_contents([vecino])
                hayAspiradora = any(isinstance(obj, Aspiradora) for obj in contenidoVecino)

                if not hayAspiradora or vecino == (1, 1):
                    vecinosValidos.append(vecino)

            if len(vecinosValidos) > 0:
                nuevaPosicion = self.random.choice(vecinosValidos)
                self.model.grid.move_agent(self, nuevaPosicion)
                self.model.movimientos += 1