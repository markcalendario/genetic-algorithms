import matplotlib.pyplot as plt

def show_graph(current_generation, current_fitness, fitness_history, best_path):
  plt.clf()
  plt.subplots_adjust(wspace=0.2)
  plt.tight_layout()

  plt.suptitle(
    f'Generation {current_generation} | Fitness {current_fitness}',
    weight="bold"
  )

  # Plot Fitness History
  plt.subplot(1, 2, 1)
  show_fitness_history(fitness_history)

  # Plot Connection of Areas
  plt.subplot(1, 2, 2)
  show_areas_connection(best_path)

def show_areas_connection(best_path):
  path = best_path
  x_values = [area.x for area in path]
  y_values = [area.y for area in path]
  plt.plot(x_values, y_values, marker='o', color="orange")

  # Connect the end and start of scatter
  plt.plot(
    [x_values[-1], x_values[0]], 
    [y_values[-1], y_values[0]], 
    color="orange"
  )

  # Annotate each point with area name
  for area, x, y in zip(path, x_values, y_values):
    plt.annotate(area.name, (x, y), textcoords="offset points", xytext=(0,3), fontsize=7)

  plt.title('Connection of PUP Areas')
  plt.xlabel('X Coordinate')
  plt.ylabel('Y Coordinate')

def show_fitness_history(fitness_history):
  plt.plot(fitness_history)
  plt.title('Fitness Timeline')
  plt.xlabel('Generation')
  plt.ylabel('Fitness')