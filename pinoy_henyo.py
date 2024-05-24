import random
import string
import matplotlib.pyplot as plt
from chart import show_fitness_history

plt.figure(figsize=(12, 5))

TARGET_WORD = input("Enter a word to guess by the guesser: ")
POPULATION_SIZE = 10
CROSSOVER_RATE = 0.4
MUTATION_RATE = 0.1
REAL_TIME = False
CHARACTER_SET = string.ascii_letters + " "

def generate_random_string():
  random_string = ''
  
  for _ in range(len(TARGET_WORD)):
    random_character = random.choice(CHARACTER_SET)
    random_string += random_character

  return random_string

def initialize_population():
  population = []

  for _ in range(POPULATION_SIZE):
    rand_string = generate_random_string()
    population.append(rand_string)

  return population

def crossover(parent1, parent2):
  # Single Point Crossover
  offspring1 = list(parent1)[:]
  offspring2 = list(parent2)[:]

  if random.random() > CROSSOVER_RATE:
    return offspring1, offspring2

  pointA = random.randint(0, len(TARGET_WORD))
  pointB = random.randint(pointA, random.randint(pointA, len(TARGET_WORD)))

  for i in range(pointA, pointB):
    temp = offspring1[i]
    offspring1[i] = offspring2[i]
    offspring2[i] = temp

  return "".join(offspring1), "".join(offspring2)

def mutate(offspring):
  # Random Resetting Mutation
  
  mutated_offspring = list(offspring)[:]

  if random.random() > MUTATION_RATE:
    return mutated_offspring

  target_gene = random.randint(0, len(offspring) - 1)
  mutated_offspring[target_gene] = random.choice(CHARACTER_SET)

  return "".join(mutated_offspring)

def fitness(chromosome):
  # 49 (a) - 49 (a) = 0 (best) [OK]
  # 50 (b) - 49 (a) = 1 ()
  cost = 0

  for i in range(len(chromosome)):
    guessN = ord(chromosome[i])
    answerN = ord(TARGET_WORD[i])
    cost += (guessN - answerN) ** 2

  return cost

population = initialize_population()
fitness_history = []
generation = 0

while True:
  population.sort(key=fitness)

  parent1 = population[0]
  parent2 = population[1]
  best_word = parent1
  best_fitness = fitness(best_word)
  fitness_history.append(best_fitness)

  child1, child2 = crossover(parent1, parent2)
  child1 = mutate(child1)
  child2 = mutate(child2)

  population[-1] = child2
  population[-2] = child1

  result = f"Generation {generation} | Fitness {best_fitness} | Word: {best_word}"
  
  if REAL_TIME:
    plt.clf()
    plt.suptitle(result, weight="bold")
    show_fitness_history(fitness_history)
    plt.pause(0.01)
  else:
    print(result)

  if best_fitness == 0:
    print(f"Found target word '{TARGET_WORD}' in {generation} generations.")
    break

  generation += 1

show_fitness_history(fitness_history)
plt.show()
