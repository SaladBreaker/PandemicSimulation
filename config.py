CONFIG = {
    "GRID": {"WIDTH": 15, "HEIGHT": 15},
    "POPULATION": {"TOTAL": 100, "INITIAL_INFECTED": 2},
    "RULES": {
        "INFECTION_PROBABILITY": {
            "0-15": 0,
            "15-30": 0.1,
            "30-50": 0.3,
            "50-70": 0.5,
            "70-150": 0.7,
        },
        "STEPS_UNTIL_RECOVERY": 10,
    },
}
