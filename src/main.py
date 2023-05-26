import genetic_algorithm
import items


container = items.Container("Hive Container")
optimizer = "speed"
ga = genetic_algorithm.GeneticAlgorithm(container, 209.7, 125, 10, optimizer)
ga.load_ga()
ga.display_best_solution()
