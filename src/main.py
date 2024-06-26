import genetic_algorithm
import items


container = items.Container("Hive Container")
optimizer = "eHP"
ga = genetic_algorithm.GeneticAlgorithm(container, 351.23, 115, 15, optimizer)
#ga.load_ga()
ga.setup_ga()
ga.run()
ga.save_ga()
ga.display_best_solution()
