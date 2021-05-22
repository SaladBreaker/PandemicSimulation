from config import CONFIG


def compute_infected(model):
    return sum([agent.is_infected for agent in model.schedule.agents])


def compute_well(model):
    return sum(
        [
            not agent.is_infected and not agent.was_infected
            for agent in model.schedule.agents
        ]
    )


def compute_were_infected(model):
    return sum([agent.was_infected for agent in model.schedule.agents])


def get_probability_based_on_age(age):
    for key in CONFIG["RULES"]["INFECTION_PROBABILITY"].keys():
        lower = int(key.split("-")[0])
        higher = int(key.split("-")[1])

        if lower <= age <= higher:
            return CONFIG["RULES"]["INFECTION_PROBABILITY"][key]
