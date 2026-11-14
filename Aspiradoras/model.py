from mesa import Model
from mesa.space import MultiGrid
from aspiradora import Aspiradora
from basura import Basura

class AspiradoraModel(Model):

    def __init__(self, width=50, height=50, num_agentes=1, porcentaje_basura=40, tiempo_maximo = 100,rng =None):
        super().__init__(rng=rng)

        self.num_agentes = num_agentes
        self.porcentaje_basura = porcentaje_basura
        self.tiempo_maximo = tiempo_maximo
        self.paso = 0

        self.grid = MultiGrid(width, height, torus=False)


        self.running = True

        total_celdas = width * height
        num_basura = int((self.porcentaje_basura / 100) * total_celdas)
        id_contador = 1

        for i in range(num_basura):
            basura = Basura(id_contador, self)
            id_contador += 1

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(basura, (x, y))

        for i in range(self.num_agentes):
            aspiradora = Aspiradora(id_contador, self)
            id_contador += 1
            self.grid.place_agent(aspiradora, (1, 1))

    def step(self):
        self.agents.do("step")

        self.paso += 1

        basura_restante = [a for a in self.agents if isinstance(a, Basura)]

        if self.paso >= self.tiempo_maximo or len(basura_restante) == 0:
            self.running = False
