# Pandemic Simulation with mesa
Simple project that uses the mesa python3 package to simulate a pandemic environment with some simple rules

# Installation
Poetry is needed to install the project.

## Using pip3
To install poetry:
```bash
pip3 install poetry
```

Create the environment:
```bash
poetry install
```

Launch the environment:
```bash
poetry shell
```

## Other methods
Check: https://python-poetry.org/docs/ for the installation command and 
then follow the same commands.


# Run
First run:
```bash
poetry shell
python server.py
```
or
```bash
poetry run python server.py 
```

then a server will open at: http://127.0.0.1:8052/


# Simulation Rules
The simulation follows some simple rules:
1. the population consists of 3 types of persons:
    
    - infected (red)
    - well (never infected) (green)
    - recovered (infected in the past) (yellow)
    
2. Each agent has an age and based on that a probability of infection is assigned to him/her

3. An infected agent spreads the virus to his/her neighbours (in relation with the above probability of infection).

4. A recovered agent can never be infected again

5. An infected agent recovers after a number of days

# How it looks
![image](https://user-images.githubusercontent.com/46823785/119233376-69567f00-bb31-11eb-95d5-1456c0901bae.png)
