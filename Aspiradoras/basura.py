from mesa import Agent

class Basura(Agent):
    def __init__(self, unique_id, model):
        super().__init__(model)
        self.unique_id = unique_id

    def step(self):
        pass