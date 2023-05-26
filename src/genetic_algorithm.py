import math

import pygad
import items
import lib


class GeneticAlgorithm:
    def __init__(self, container: items.Container, armor: float, quality: float, potential: int, optimizer="eHP"):
        self.container = container
        self.armor = armor
        self.artifacts = lib.load_mem("../resources/artifacts.json")
        self.quality = quality
        self.potential = potential
        self.GA = None
        self.amount_upgrades = math.floor(self.potential / 5)
        self.num_genes = self.container.cells * (self.amount_upgrades + 1)
        self.optimizer = optimizer

    def fitness_func(self, ga_instance, solution, solution_idx):
        artifacts, valid = self.get_artifacts_from_solution(solution)

        if not valid:
            return -1

        vitality = 100
        bullet_res = self.armor
        heal_effect = 0
        spd = 0
        stamina_regen = 0
        rad = 0
        bio = 0
        temp = 0
        psy = 0
        frost = 0

        for art in artifacts:
            vitality += art.vitality
            bullet_res += art.bullet_resistance
            heal_effect += art.healing_effectiveness
            spd += art.movement_speed
            stamina_regen += art.stamina_regen
            rad += art.radiation
            bio += art.biological_infection
            temp += art.temperature
            psy += art.psy_emissions
            frost += art.frost

        if rad > 0:
            rad *= (1 - self.container.protection)
            rad = round(rad, 2)
        if bio > 0:
            bio *= (1 - self.container.protection)
            bio = round(bio, 2)
        if temp > 0:
            temp *= (1 - self.container.protection)
            temp = round(temp, 2)
        if psy > 0:
            psy *= (1 - self.container.protection)
            psy = round(psy, 2)

        if rad >= 0.5 or bio >= 0.5 or temp >= 0.5 or psy >= 1.5 or frost >= 1:
            return -1

        if self.optimizer == "eHP":
            return round((100 + bullet_res) * (vitality / 100), 2)
        elif self.optimizer == "max_speed":
            return spd
        elif self.optimizer == "speed":
            return spd + stamina_regen
        elif self.optimizer == "heal":
            return round((100 + bullet_res) * (vitality / 100) + heal_effect, 2)
        elif self.optimizer == "max_heal":
            return heal_effect
        else:
            raise ValueError("Invalid optimizer")

    def get_artifacts_from_solution(self, solution):
        artifacts = []
        cur_properties = []
        artifact = None
        valid = True

        for i in range(len(solution)):
            cur_solution = solution[i]
            if i % (self.amount_upgrades + 1) == 0:
                artifact_name = list(self.artifacts.keys())[cur_solution]
                artifact = items.Artifact(artifact_name, self.quality, self.potential)
                artifacts.append(artifact)

            else:
                extra_properties = artifact.extra_properties
                if cur_solution > len(list(extra_properties.keys())) - 1:
                    valid = False
                    break
                else:
                    property_index = list(extra_properties.keys())[cur_solution]
                    cur_properties.append(property_index)

            if len(cur_properties) != len(set(cur_properties)):
                valid = False

            if len(cur_properties) == self.amount_upgrades:
                artifact.set_additional_properties(cur_properties)
                cur_properties = []

        return artifacts, valid

    def calculate_gene_space(self, min, max):
        gene_space = []
        for i in range(self.container.cells):
            gene_space.append({"low": min, "high": max})
            for j in range(self.amount_upgrades):
                gene_space.append([0, 1, 2, 3])

        return gene_space

    def setup_ga(self):
        fitness_function = self.fitness_func

        num_generations = 150
        num_parents_mating = 20

        sol_per_pop = 100

        min_value = 0
        max_value = len(self.artifacts)
        gene_type = int
        gene_space = self.calculate_gene_space(min_value, max_value)

        parent_selection_type = "sss"
        keep_parents = 2

        crossover_type = "single_point"

        mutation_type = "random"
        mutation_probability = 0.1

        self.GA = pygad.GA(num_generations, num_parents_mating, fitness_function, sol_per_pop=sol_per_pop,
                           num_genes=self.num_genes,
                           random_mutation_min_val=min_value, random_mutation_max_val=max_value,
                           gene_type=gene_type, gene_space=gene_space, parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type, mutation_type=mutation_type,
                           mutation_by_replacement=True,
                           mutation_probability=mutation_probability)

    def run(self):
        self.GA.run()

    def save_ga(self):
        self.GA.save(f"../resources/saves/{self.container.name}-{self.optimizer}")

    def load_ga(self):
        self.GA = pygad.load(f"../resources/saves/{self.container.name}-{self.optimizer}")

    def display_best_solution(self):
        solution, solution_fitness, solution_idx = self.GA.best_solution()
        sol_str = ""
        solution = solution
        artifacts = self.get_artifacts_from_solution(solution)[0]
        for art in artifacts:
            sol_str += f"{art.to_string()}\n"

        print(f"Best solution:\n{sol_str}")
        print(f"Fitness of best solution: {solution_fitness}")
        return solution
