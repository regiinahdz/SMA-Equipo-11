# Programa: define un agente de basura para la simulacion de limpieza.
# Autores: Regina Hernández Moreno - A01802688; Ricardo Oved Cornejo Castro - A01803272
# Fecha de creacion/modificacion: 16/11/2026

from mesa import Agent


class Basura(Agent):
    # Inicializa un agente de basura.
    # Parametros: self, instancia actual; uniqueId, identificador solicitado; model, modelo al que pertenece.
    # Retorno: None.
    def __init__(self, uniqueId, model):
        super().__init__(model)
        self.uniqueId = uniqueId

    # Mantiene al agente de basura sin acciones durante cada paso.
    # Parametros: self, instancia actual.
    # Retorno: None.
    def step(self):
        pass