from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule

from models import PandemicModel

from config import CONFIG


def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.5}

    if agent.is_infected:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    elif agent.was_infected:
        portrayal["Color"] = "yellow"
        portrayal["Layer"] = 2
    else:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 1

    return portrayal


grid = CanvasGrid(
    agent_portrayal, CONFIG["GRID"]["WIDTH"], CONFIG["GRID"]["HEIGHT"], 500, 500
)

chart = ChartModule(
    [
        {"Label": "infected", "Color": "Red"},
        {"Label": "well", "Color": "Green"},
        {"Label": "recovered", "Color": "Yellow"},
    ],
    data_collector_name="data_collector",
)

server = ModularServer(
    PandemicModel,
    [grid, chart],
    "Pandemic Model",
    {
        "number_of_agents": CONFIG["POPULATION"]["TOTAL"],
        "initial_infected": CONFIG["POPULATION"]["INITIAL_INFECTED"],
        "width": CONFIG["GRID"]["WIDTH"],
        "height": CONFIG["GRID"]["HEIGHT"],
    },
)

server.port = 8052
server.launch()
