import genetic_algorithm
import items


container = items.Container("KZS-5")
ga = genetic_algorithm.GeneticAlgorithm(container, 209.7, 125, 10, "speed")
ga.display_best_solution()
