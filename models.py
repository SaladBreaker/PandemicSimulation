from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from utils import *
from config import CONFIG


# Dummy probabilities just for the proof of concept, those do net reflect real life probabilities!
# an infected agent will recover after 3 steps and will gain absolute immunity


class PandemicModel(Model):
    """A model with some number of agents."""

    def __init__(
        self, number_of_agents: int, initial_infected: float, width: int, height: int
    ):
        super(PandemicModel, self).__init__()

        self.number_of_agents = number_of_agents
        self.initial_infected = initial_infected

        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True

        # Create agents
        for i in range(self.number_of_agents):

            name = f"Agent_{i}"
            if i < initial_infected:
                agent = PersonAgent(
                    name, self, age=self.random.randrange(100), is_infected=True
                )

            else:
                agent = PersonAgent(
                    name, self, age=self.random.randrange(100), is_infected=False
                )

            self.schedule.add(agent)

            # Add the agent to a random grid cell
            self.grid.place_agent(
                agent,
                (
                    self.random.randrange(self.grid.width),
                    self.random.randrange(self.grid.height),
                ),
            )

        # create a data collector for statistical reasons
        self.data_collector = DataCollector(
            model_reporters={
                "infected": compute_infected,
                "well": compute_well,
                "recovered": compute_were_infected,
            },
            agent_reporters={
                "age": "age",
                "was_infected": "was_infected",
                "is_infected": "is_infected",
            },
        )

    def step(self):
        self.data_collector.collect(self)
        self.schedule.step()


class PersonAgent(Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, unique_id: str, model: Model, age: int, is_infected: bool):
        super().__init__(unique_id, model)
        self.age = age
        self.infection_probability = get_probability_based_on_age(age)

        self.days_until_recovery = None
        self.is_infected = is_infected
        self.was_infected = False

        if is_infected:
            self.get_virus()

    def step(self):
        self.move()

        if self.is_infected:
            self.days_until_recovery -= 1

            if self.is_recovered():
                self.cured()

            else:
                self.spread_virus()

    def get_virus(self):
        self.is_infected = True
        self.days_until_recovery = CONFIG["RULES"]["STEPS_UNTIL_RECOVERY"]
        self.was_infected = True

    def cured(self):
        self.is_infected = False
        self.infection_probability = 0

    def is_recovered(self):
        if self.days_until_recovery == 0:
            return True

        return False

    def spread_virus(self):
        # gets agents near him
        for cellmate in self.model.grid.get_cell_list_contents(
            [self.pos]
        ):  # type: PersonAgent
            if (
                not cellmate.was_infected
                and self.random.random() > cellmate.infection_probability
            ):
                cellmate.get_virus()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore=True, include_center=False  # 8
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
