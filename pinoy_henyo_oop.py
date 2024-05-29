import string, random
import matplotlib.pyplot as plt
from chart import show_fitness_history

plt.figure(figsize=(12, 5))
REAL_TIME = False

## GAME MASTER ##

class GameMaster:
  def get_target_word_length(self):
    return len(self.target_word)
  
  def ask_word(self):
    self.target_word = input("Enter a word to guess (alphabets and space only): ")
    return len(self.target_word)
  
  def get_acii_of_string(self, str):
    ascii_equivalent = []
    
    for char in range(len(str)):
      ascii_equivalent.append(ord(str[char]))

    return ascii_equivalent
  
  def compute_cost(self, guess_word):
    target_word_ascii = self.get_acii_of_string(self.target_word)
    guess_word_ascii = self.get_acii_of_string(guess_word)

    cost = 0

    for i in range(len(self.target_word)):
      guessN = guess_word_ascii[i]
      targetN = target_word_ascii[i]

      cost += (guessN - targetN) ** 2
    
    return cost

## GUESSER ##

class Guesser:
  def __init__(self, word_length, game_master):
    self.MAX_GENERATION = 100
    self.MAX_POPULATION = 10
    self.CROSSOVER_RATE = 0.4
    self.MUTATION_RATE = 0.1
    self.WORD_LENGTH = word_length
    self.CHARACTER_SET = string.ascii_letters + " "
    self.game_master = game_master

  def start_guessing(self):
    population = self.initialize_population()
    fitness_history = []

    for generation in range(0, self.MAX_GENERATION + 1):
      population.sort(key=self.game_master.compute_cost)

      parent1 = population[0]
      parent2 = population[1]

      best_word = parent1
      best_word_cost = self.game_master.compute_cost(best_word)
      fitness_history.append(best_word_cost)

      result = f"Generation {generation} | Fitness {best_word_cost} | Word: {best_word}"
  
      if REAL_TIME:
        plt.clf()
        plt.suptitle(result, weight="bold")
        show_fitness_history(fitness_history)
        plt.pause(0.01)
      else:
        print(result)

      if best_word_cost == 0:
        print(f"Found target word '{best_word}' in {generation} generations.")
        break


      child1, child2 = self.crossover(parent1, parent2)
      child1 = self.mutate(child1)
      child2 = self.mutate(child2)
      
      population[-2] = child1
      population[-1] = child2

    show_fitness_history(fitness_history)
    plt.show()


  def initialize_population(self):
    population = []

    for _ in range(self.MAX_POPULATION):
      rand_string = ""

      for _ in range(self.WORD_LENGTH):
        rand_string += random.choice(self.CHARACTER_SET)
      
      population.append(rand_string)
    
    return population

  def crossover(self, parent1, parent2):
    # Single Point Crossover
    offspring1 = list(parent1)[:]
    offspring2 = list(parent2)[:]

    if random.random() > self.CROSSOVER_RATE:
      return offspring1, offspring2

    pointA = random.randint(0, self.WORD_LENGTH)
    pointB = random.randint(pointA, random.randint(pointA, self.WORD_LENGTH))

    for i in range(pointA, pointB):
      temp = offspring1[i]
      offspring1[i] = offspring2[i]
      offspring2[i] = temp

    return "".join(offspring1), "".join(offspring2)
  
  def mutate(self, offspring):
    # Random Resetting Mutation
    
    mutated_offspring = list(offspring)[:]

    if random.random() > self.MUTATION_RATE:
      return mutated_offspring

    target_gene = random.randint(0, len(offspring) - 1)
    mutated_offspring[target_gene] = random.choice(self.CHARACTER_SET)

    return "".join(mutated_offspring)

game_master = GameMaster()
word_length = game_master.ask_word()

guesser = Guesser(word_length, game_master)
guesser.start_guessing()