# Programa: crea y ejecuta el modelo de la simulacion de aspiradoras.
# Autores: Regina Hernández Moreno - A01802688; Ricardo Oved Cornejo Castro - A01803272
# Fecha de creacion/modificacion: 16/11/2026

from mesa import Model
from mesa.space import MultiGrid
from aspiradora import Aspiradora
from basura import Basura


class AspiradoraModel(Model):

    # Configura la cuadricula, la basura inicial y los agentes aspiradores.
    # Parametros: self, instancia actual; width, ancho de la cuadricula; height, alto de la cuadricula;
    # numAgentes, cantidad de aspiradoras; porcentajeBasura, porcentaje inicial de celdas con basura;
    # tiempoMaximo, limite de pasos; rng, semilla aleatoria opcional.
    # Retorno: None.
    def __init__(
        self,
        width=50,
        height=50,
        numAgentes=1,
        porcentajeBasura=40,
        tiempoMaximo=100,
        rng=None,
    ):
        if rng is not None:
            rng = int(rng)

        super().__init__(rng=rng)

        self.numAgentes = numAgentes
        self.porcentajeBasura = porcentajeBasura
        self.tiempoMaximo = tiempoMaximo
        self.paso = 0
        self.movimientos = 0
        self.totalCeldas = width * height

        self.grid = MultiGrid(width, height, torus=False)
        self.running = True

        numBasura = int((self.porcentajeBasura / 100) * self.totalCeldas)
        idContador = 1
        coordenadas = [
            (x, y)
            for x in range(self.grid.width)
            for y in range(self.grid.height)
        ]
        posicionesBasura = self.random.sample(coordenadas, numBasura)

        for posicion in posicionesBasura:
            basura = Basura(idContador, self)
            idContador += 1
            self.grid.place_agent(basura, posicion)

        for _ in range(self.numAgentes):
            aspiradora = Aspiradora(idContador, self)
            idContador += 1
            self.grid.place_agent(aspiradora, (1, 1))

    # Ejecuta un paso y detiene el modelo al alcanzar su limite o limpiar la basura.
    # Parametros: self, instancia actual.
    # Retorno: None.
    def step(self):
        self.agents.do("step")
        self.paso += 1

        basuraRestante = [agent for agent in self.agents if isinstance(agent, Basura)]

        if self.paso >= self.tiempoMaximo or len(basuraRestante) == 0:
            self.running = False

    # Calcula las metricas finales de la simulacion.
    # Parametros: self, instancia actual.
    # Retorno: diccionario con pasos, porcentaje de celdas limpias y movimientos.
    def obtenerEstadisticas(self):
        basuraRestante = sum(
            1 for agent in self.agents if isinstance(agent, Basura)
        )
        porcentajeLimpio = 0.0
        if self.totalCeldas > 0:
            porcentajeLimpio = round(
                ((self.totalCeldas - basuraRestante) / self.totalCeldas) * 100,
                2,
            )

        return {
            "pasos": self.paso,
            "movimientos": self.movimientos,
            "celdasLimpias": self.totalCeldas - basuraRestante,
            "totalCeldas": self.totalCeldas,
            "porcentajeLimpias": porcentajeLimpio,
        }
