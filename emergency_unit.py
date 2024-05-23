import random, math
import matplotlib.pyplot as plt
from chart import show_fitness_history

plt.figure(figsize=(12, 6))

POPULATION_SIZE = 10
MAX_GENERATIONS = 50000
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.4
REAL_TIME = False
CITY_MATRIX = [
    [5, 2, 4, 8, 9, 0, 3, 3, 8, 7],
    [5, 5, 3, 4, 4, 6, 4, 1, 9, 1],
    [4, 1, 2, 1, 3, 8, 7, 8, 9, 1],
    [1, 7, 1, 6, 9, 3, 1, 9, 6, 9],
    [4, 7, 4, 9, 9, 8, 6, 5, 4, 2],
    [7, 5, 8, 2, 5, 2, 3, 9, 8, 2],
    [1, 4, 0, 6, 8, 4, 0, 1, 2, 1],
    [1, 5, 2, 1, 2, 8, 3, 3, 6, 2],
    [4, 5, 9, 6, 3, 9, 7, 6, 5, 10],
    [0, 6, 2, 8, 7, 1, 2, 1, 5, 3]
]
MAX_CITY_ROWS = len(CITY_MATRIX)
MAX_CITY_COLS = len(CITY_MATRIX[0])

def generate_population():
  population = []

  for _ in range(POPULATION_SIZE):
    randX = random.randint(0, MAX_CITY_ROWS - 1)
    randY = random.randint(0, MAX_CITY_COLS - 1)
    population.append([randX, randY])

  return population

def fitness(coordinates):
  fitness = 0

  for x in range(MAX_CITY_ROWS - 1):
    for y in range(MAX_CITY_COLS - 1):
      fitness += CITY_MATRIX[x][y] * (math.sqrt((x + 1 - coordinates[0]) ** 2) + math.sqrt((y + 1 - coordinates[1]) ** 2))
  
  return fitness

def crossover(parent1, parent2):
  offspring1 = parent1[:]
  offspring2 = parent2[:]
  
  if random.random() > CROSSOVER_RATE:
    return offspring1, offspring2
  
  return offspring2, offspring1

def mutate(chromosome):
  mutated_chromosome = chromosome[:]

  if random.random() > MUTATION_RATE:
    return mutated_chromosome

  mutated_chromosome[0] = random.randint(0, MAX_CITY_ROWS - 1)
  mutated_chromosome[1] = random.randint(0, MAX_CITY_COLS - 1)

  return mutated_chromosome

def real_coordinates(coordinates):
  real_coordinates = [coordinates[0] + 1, coordinates[1] + 1] 
  return real_coordinates

population = generate_population()
fitness_history = []

for generation in range(1, MAX_GENERATIONS + 1):
  population.sort(key=fitness)
  best_fitness = fitness(population[0])
  fitness_history.append(best_fitness)

  parent1 = population[0]
  parent2 = population[1]

  children = crossover(parent1, parent2)
  child1 = mutate(children[0])
  child2 = mutate(children[1])

  population[-1] = child1
  population[-2] = child2

  result = f"Generation {generation} | Fitness {best_fitness} | Coordinate {real_coordinates(population[0])}"

  if REAL_TIME:
    plt.clf()
    plt.suptitle(result, weight="bold")
    show_fitness_history(fitness_history)
    plt.pause(0.01)
  else:
    print(result)

show_fitness_history(fitness_history)
plt.show()
