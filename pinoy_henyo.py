import random
import string
import matplotlib.pyplot as plt
from chart import show_fitness_history

plt.figure(figsize=(12, 5))

TARGET_WORD = input("Enter a word to guess by the guesser: ")
POPULATION_SIZE = 100
MUTATION_RATE = 0.9
CROSSOVER_RATE = 0.9
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
  # Create copy of the parents so it won't change the original value
  offspring1 = list(parent1)[:]
  offspring2 = list(parent2)[:]
  
  if random.random() > CROSSOVER_RATE:
    return offspring1, offspring2
  
  # Choose two random crossover points
  size = len(parent1)
  crossover_point1 = random.randint(0, size - 1)
  crossover_point2 = random.randint(crossover_point1 + 1, size)

  # Initialize dictionaries to keep track of character mapping
  mapping1 = {}
  mapping2 = {}

  # Apply crossover between the two crossover points
  for i in range(crossover_point1, crossover_point2):
    # Get the values from parents
    temp1 = parent2[i]
    temp2 = parent1[i]

    # Swap the values in the offspring
    offspring1[i] = temp1
    offspring2[i] = temp2

    # Update mapping dictionaries
    mapping1[temp1] = temp2
    mapping2[temp2] = temp1

  # Apply mapping to resolve duplicates
  for i in range(size):
    if i < crossover_point1 or i >= crossover_point2:
      if offspring1[i] in mapping1:
        offspring1[i] = mapping1[offspring1[i]]
      if offspring2[i] in mapping2:
        offspring2[i] = mapping2[offspring2[i]]

  return ''.join(offspring1), ''.join(offspring2)

def mutate(string):
  # Create copy of the string so it won't change the original value
  mutated_string = list(string)[:]

  if random.random() > MUTATION_RATE:
    return mutated_string
  
  target_pos = random.randint(0, len(string))

  for i in range(len(mutated_string)):
    if target_pos == i:
      mutated_string[i] = random.choice(CHARACTER_SET)

  return ''.join(mutated_string)

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

  population[-1:] = child1, child2

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
