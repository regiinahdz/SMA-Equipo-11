    # Programa: visualiza una simulacion de agentes aspiradores y basura.
# Autores: Regina Hernández Moreno - A01802688; Ricardo Oved Cornejo Castro - A01803272
# Fecha de creacion/modificacion: 16/11/2026

import solara
from model import AspiradoraModel
from mesa.visualization import SolaraViz, SpaceRenderer
from mesa.visualization.components import AgentPortrayalStyle
from mesa.visualization.utils import update_counter
from aspiradora import Aspiradora
from basura import Basura


# Muestra las estadisticas actuales del modelo de simulacion.
# Parametros: model, modelo de aspiradoras del que se leen las estadisticas.
# Retorno: componente Solara con el resumen de pasos, movimientos y celdas limpias.
@solara.component
def panelInformacion(model):
    update_counter.get()
    datos = model.obtenerEstadisticas()
    solara.Markdown(
        f"""
### Informacion de la simulacion
- Tiempo transcurrido (pasos): {datos["pasos"]}
- Movimientos totales realizados: {datos["movimientos"]}
- Celdas limpias: {datos["celdasLimpias"]} de {datos["totalCeldas"]} cuadros limpios
"""
    )


# Describe la apariencia de cada tipo de agente.
# Parametros: agent, agente cuya apariencia se va a definir.
# Retorno: estilo visual correspondiente al tipo de agente.
def agentPortrayal(agent):
    if isinstance(agent, Aspiradora):
        return AgentPortrayalStyle(color="blue", marker="o", size=50)
    if isinstance(agent, Basura):
        return AgentPortrayalStyle(color="grey", marker="s", size=20)
    return None


# Ajusta la proporcion y oculta las marcas de los ejes.
# Parametros: ax, ejes de Matplotlib que se van a configurar.
# Retorno: None.
def postProcess(ax):
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])


model_params = {
    "rng": {
        "type": "InputText",
        "value": 42,
        "label": "Semilla aleatoria",
    },
    "width": {
        "type": "SliderInt",
        "value": 20,
        "label": "Ancho (M)",
        "min": 5,
        "max": 60,
        "step": 1,
    },
    "height": {
        "type": "SliderInt",
        "value": 20,
        "label": "Alto (N)",
        "min": 5,
        "max": 60,
        "step": 1,
    },
    "numAgentes": {
        "type": "SliderInt",
        "value": 3,
        "label": "Numero de agentes",
        "min": 1,
        "max": 50,
        "step": 1,
    },
    "porcentajeBasura": {
        "type": "SliderInt",
        "value": 40,
        "label": "Porcentaje de basura inicial",
        "min": 1,
        "max": 100,
        "step": 1,
    },
    "tiempoMaximo": {
        "type": "SliderInt",
        "value": 60,
        "label": "Tiempo maximo",
        "min": 20,
        "max": 600,
        "step": 1,
    },
}

model1 = AspiradoraModel()
renderer = SpaceRenderer(model1, backend="matplotlib").setup_agents(agentPortrayal)
renderer.render()
renderer.post_process = postProcess

page = SolaraViz(
    model1,
    renderer,
    model_params=model_params,
    components=[panelInformacion],
    name="Aspiradoras",
)
page  # noqa
