import random
import math
from chart import show_graph
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

NUM_AREAS = 10
MAX_GENERATIONS = 5000
POPULATION_SIZE = 10
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.4
REAL_TIME = False

class Area:
  def __init__(self, name, x, y):
    self.name = name
    self.x = x
    self.y = y

areas = [
  Area("Gate", 2, 5),
  Area("Court", 7, 15),
  Area("Catwalk", 15, 8),
  Area("Obelisk", 13, 12),
  Area("Lagoon", 19, 15),
  Area("Gym", 2, 10),
  Area("Oval", 5, 9),
  Area("Chapel", 7, 18),
  Area("Pool", 13, 5),
  Area("Main Building", 20, 4),
]

def calculate_distance(area1, area2):
  dx = area1.x - area2.x
  dy = area1.y - area2.y
  return math.sqrt(dx * dx + dy * dy)

def random_population():
  population = []

  for _ in range(POPULATION_SIZE):
    path = random.sample(areas, len(areas))
    population.append(path)

  return population

def fitness(path):
  total_fitness = 0

  for i in range(len(path) - 1):
    area1 = path[i]
    area2 = path[i + 1]
    distance = calculate_distance(area1, area2)
    total_fitness += distance

  return total_fitness

def crossover(parent1, parent2):
  offspring1 = parent1[:]
  offspring2 = parent2[:]

  if random.random() > CROSSOVER_RATE:
    return offspring1, offspring2
  
  # Choose two random crossover points
  size = len(parent1)
  crossover_point1 = random.randint(0, size)
  crossover_point2 = random.randint(0, size - 1)

  if crossover_point2 >= crossover_point1:
    crossover_point2 += 1
  else:
    crossover_point1, crossover_point2 = crossover_point2, crossover_point1

  # Apply crossover between the two crossover points
  for i in range(crossover_point1, crossover_point2):
    # Get the value from parent2
    temp1 = parent2[i]
    temp2 = parent1[i]
    # Swap the values in the offspring
    index1 = offspring1.index(temp1)
    index2 = offspring2.index(temp2)
    offspring1[i], offspring1[index1] = offspring1[index1], offspring1[i]
    offspring2[i], offspring2[index2] = offspring2[index2], offspring2[i]

  return offspring1, offspring2

def mutate(path):
  mutated_path = path[:]

  if random.random() < MUTATION_RATE:
    # Select two random positions to swap
    pos1, pos2 = random.sample(range(len(mutated_path)), 2)
    # Swap the elements at the selected positions
    mutated_path[pos1], mutated_path[pos2] = mutated_path[pos2], mutated_path[pos1]

  return mutated_path

population = random_population()
fitness_history = []

for generation in range(1, MAX_GENERATIONS + 1):
  population.sort(key=fitness)
  best_fitness = fitness(population[0])

  fitness_history.append(best_fitness)

  parent1 = population[0]
  parent2 = population[1]

  children = crossover(parent1, parent2)

  child1 = children[0]
  child2 = children[1]

  child1 = mutate(child1)
  child2 = mutate(child2)

  population[-1:] = child1, child2

  if REAL_TIME:
    show_graph(generation, best_fitness, fitness_history, population[0])
    plt.pause(0.01)
  else:
    print(f"Generation {generation} | Fitness {best_fitness}")

show_graph(MAX_GENERATIONS, fitness(population[0]), fitness_history, population[0])
plt.show()