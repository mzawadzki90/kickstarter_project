import numpy as np

from genetic_algorithm.genome import Genome


class PopulationInitializer:
    population_size: int
    genome: Genome

    def __init__(self, population_size: int, genome: Genome):
        self.population_size = population_size
        self.genome = genome

    def init_population(self) -> np.ndarray:
        pass


class RandomInitialization(PopulationInitializer):

    def init_population(self) -> np.ndarray:
        population = np.random.uniform(low=self.genome.gene_low, high=self.genome.gene_high,
                                       size=(self.population_size, self.genome.dimension))
        print("Generation: 1; Population: ", population)
        return population
