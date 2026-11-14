#from mesa.examples.basic.conways_game_of_life.model import ConwaysGameOfLife
from model import AspiradoraModel

from mesa.visualization import (
    SolaraViz,
    SpaceRenderer,
)
from mesa.visualization.components import AgentPortrayalStyle


from aspiradora import Aspiradora
from basura import Basura

def agent_portrayal(agent):
    # Si es Aspiradora, la dibujamos como un círculo azul
    if isinstance(agent, Aspiradora):
        return AgentPortrayalStyle(
            color="blue",
            marker="o",
            size=50,
        )
    # Si es Basura, como un cuadrado gris
    elif isinstance(agent, Basura):
        return AgentPortrayalStyle(
            color="grey",
            marker="s",
            size=20,
        )


def post_process(ax):
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])


model_params = {
    "rng": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
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
    "num_agentes": {
        "type": "SliderInt",
        "value": 3,
        "label": "Número de Agentes",
        "min": 1,
        "max": 50,
        "step": 1,
    },
    "porcentaje_basura": {
        "type": "SliderInt",
        "value": 40,
        "label": "Porcentaje de Basura Inicial",
        "min": 1,
        "max": 100,
        "step": 1,
    },
    "tiempo_maximo": {
        "type": "SliderInt",
        "value": 60,
        "label": "Tiempo maximo",
        "min": 20,
        "max": 600,
        "step": 1,
    }
}

# Create initial model instance
model1 = AspiradoraModel()

renderer = SpaceRenderer(model1, backend="matplotlib").setup_agents(agent_portrayal)
renderer.render()
renderer.post_process = post_process

# Create the SolaraViz page. This will automatically create a server and display the
# visualization elements in a web browser.
# Display it using the following command in the example directory:
# solara run app.py
# It will automatically update and display any changes made to this file
page = SolaraViz(
    model1,
    renderer,
    model_params=model_params,
    name="Aspiradoras",
)
page  # noqa
