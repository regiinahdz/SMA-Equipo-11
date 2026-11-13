from mesa import Agent


class Basura(Agent):
    def __init__(self, unique_id, model):
        # Todo agente necesita un ID único y conocer el modelo en el que vive
        super().__init__(unique_id, model)

        # Aquí podemos añadir más atributos después, como batería o basura recolectada

    def step(self):
        # Aquí irá la lógica de limpieza y movimiento
        pass