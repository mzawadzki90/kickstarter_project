import numpy as np

from genetic_algorithm.genome import Genome


class PopulationInitializer:
    population_size: int
    genome: Genome

    def __init__(self, population_size: int, genome: Genome):
        self.population_size = population_size
        self.genome = genome

    def _init_population(self, low: float, high: float) -> np.ndarray:
        pass


class RandomInitialization(PopulationInitializer):

    def __init_population(self, low: float, high: float) -> np.ndarray:
        population = np.random.uniform(low=low, high=high, size=(self.population_size, self.genome.dimension))
        print("Generation: 1; Population: ", population)
        return population
