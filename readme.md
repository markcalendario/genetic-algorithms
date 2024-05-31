# Applications of Genetic Algorithms

This repository contains 3 examples of genetic algorithm including `word guessing game`, `emergency unit`, and `travelling salesman problem`. It was an activity for Introduction to Artificial Intelligence subject.

## Travelling Salesman Problem

The source code for TSP can be found at `travelling_salesman.py`. It looks for the best route by computing the optimal route for a given set of cities, aiming to minimize the total distance traveled by a traveling salesman. This implementation utilizes a Genetic Algorithm (GA) approach to find an approximate solution to the Traveling Salesman Problem (TSP).

### Specification

- `NUM_AREAS = 10`
- `MAX_GENERATIONS = 5000`
- `POPULATION_SIZE = 10`
- `MUTATION_RATE = 10%`
- `CROSSOVER_RATE = 40%`

### Techniques

- Crossover: `Partially Mapped Crossover`
- Mutation: `Swap Mutation`
- Stopping Function: `5000 Generations`
- Chromosome Encoding: `Coordinates, [x, y]`

### Cost Function

![TSP Cost Function](https://raw.githubusercontent.com/markcalendario/genetic-algorithms/main/docs/tsp/cost-formula.png)

### Plant UML

![TSP Plant UML](https://raw.githubusercontent.com/markcalendario/genetic-algorithms/main/docs/tsp/plant-uml.png)

## Pinoy Henyo (Word Guessing Game)

The provided source code (`word_guessing.py`) implements a Word Guessing Game using a Genetic Algorithm (GA) approach. In this game, the GA evolves a population of candidate words to approximate a target word specified by the user.

### Specification

- `NUM_AREAS = 10`
- `MAX_GENERATIONS = 5000`
- `POPULATION_SIZE = 10`
- `MUTATION_RATE = 10%`
- `CROSSOVER_RATE = 40%`
- `CHARACTER_SET = (a-z)+ | (A-Z)+ | [SPACE]`

### Techniques

- Crossover: `Single Point Crossover`
- Mutation: `Random Resetting`
- Stopping Function: `5000 Generations || Cost = 0`
- Chromosome Encoding: `ASCII`

### Cost Function

![TSP Cost Function](https://raw.githubusercontent.com/markcalendario/genetic-algorithms/main/docs/word-guessing-game/cost-formula.png)

### Plant UML

![TSP Plant UML](https://raw.githubusercontent.com/markcalendario/genetic-algorithms/main/docs/word-guessing-game/plant-uml.png)

### Specification

- `NUM_AREAS = 10`
- `MAX_GENERATIONS = 5000`
- `POPULATION_SIZE = 10`
- `MUTATION_RATE = 10%`
- `CROSSOVER_RATE = 40%`

### Techniques

- Crossover: `Partially Mapped Crossover`
- Mutation: `Swap Mutation`
- Stopping Function: `5000 Generations`
- Chromosome Encoding: `Coordinates, [x, y]`

### Cost Function

![TSP Cost Function](https://raw.githubusercontent.com/markcalendario/genetic-algorithms/main/docs/tsp/cost-formula.png)

### Plant UML

![TSP Plant UML](https://raw.githubusercontent.com/markcalendario/genetic-algorithms/main/docs/tsp/plant-uml.png)

## Pinoy Henyo (Word Guessing Game)

The provided source code (`word_guessing.py`) implements a Word Guessing Game using a Genetic Algorithm (GA) approach. In this game, the GA evolves a population of candidate words to approximate a target word specified by the user.

### Specification

- `MAX_GENERATION = 5000`
- `MAX_POPULATION = 10`
- `MUTATION_RATE = 10%`
- `CROSSOVER_RATE = 40%`
- `CHARACTER_SET = (a-z)+ | (A-Z)+ | [SPACE]`

### Techniques

- Crossover: `Single Point Crossover`
- Mutation: `Random Resetting`
- Stopping Function: `5000 Generations || Cost = 0`
- Chromosome Encoding: `ASCII`

### Cost Function

![WGG Cost Function](https://raw.githubusercontent.com/markcalendario/genetic-algorithms/main/docs/word-guessing-game/cost-formula.png)

### Plant UML

![WGG Plant UML](https://raw.githubusercontent.com/markcalendario/genetic-algorithms/main/docs/word-guessing-game/plant-uml.png)

## Emergency Unit

This project implements a Genetic Algorithm (GA) to optimize the location of emergency units within a given city grid. The objective is to find the optimal placement of emergency units to minimize emergency response time, considering the frequency of emergencies across different locations within the city.

### Specification

- `MAX_GENERATION = 100`
- `POPULATION_SIZE = 10`
- `MUTATION_RATE = 10%`
- `CROSSOVER_RATE = 40%`

### Techniques

- Crossover: `Single Point Crossover`
- Mutation: `Random Resetting`
- Stopping Function: `100 Generations`
- Chromosome Encoding: `Coordinates, [x, y]`

### Cost Function

![EU Cost Function](https://raw.githubusercontent.com/markcalendario/genetic-algorithms/main/docs/emergency-unit/cost-formula.png)

### Plant UML

![EU Plant UML](https://raw.githubusercontent.com/markcalendario/genetic-algorithms/main/docs/emergency-unit/plant-uml.png)

# How it Works

1. **Initialization**: Randomly generates an initial population of routes, where each route represents a possible solution to the TSP.
2. **Evaluation**: Evaluates the fitness of each chromosomes based on their fitness or cost.

3. **Parent Selection**: Selects chromomes from the current population to be parents based on their fitness or cost. Chromosomes with lower total cost or fintess (means better) are more likely to be selected.

4. **Crossover**: Combines pairs of parents to create new offsprings. This is done by exchanging segments of the parents.

5. **Mutation**: Introduces random changes to the offspring routes to maintain genetic diversity in the population.

6. **Appending**: Appends the mutated offsprings to the population pool, removing the chromosomes with the worst fitness or cost.

7. **Termination / Stopping Function**: The algorithm terminates when a stopping condition is met, such as reaching a maximum number of generations or finding a satisfactory cost.
