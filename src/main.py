import genetic_algorithm
import items


container = items.Container("Hive Container")
ga = genetic_algorithm.GeneticAlgorithm(container, 209.7, 125, 10, "speed")
ga.save_ga("speed")
ga.display_best_solution()
