from typing import Callable

import numpy as np

from genetic_algorithm.crossover import OnePointCrossover, OnePointBinaryCrossover
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm
from genetic_algorithm.genome import Genome
from genetic_algorithm.initialization import RandomInitialization
from genetic_algorithm.mutation import RandomMutation, FlipBitMutation
from genetic_algorithm.parent_selection import TournamentSelection


class GeneticAlgorithmImpl(GeneticAlgorithm):

    def init_population(self, ):
        return RandomInitialization(self.population_size, self.genome).init_population()

    def select_parents(self, fitness):
        return TournamentSelection().select_parents(self.population, fitness)

    def crossover(self, parents):
        return OnePointCrossover().crossover(parents)

    def mutate(self, crossovers):
        return RandomMutation().mutate(crossovers)


class GeneticAlgorithmImpl2(GeneticAlgorithm):

    def init_population(self, ):
        return RandomInitialization(self.population_size, self.genome).init_population()

    def select_parents(self, fitness):
        return TournamentSelection().select_parents(self.population, fitness)

    def crossover(self, parents):
        return OnePointBinaryCrossover().crossover(parents)

    def mutate(self, crossovers):
        return FlipBitMutation().mutate(crossovers)


quadratic_rank: Callable[[np.ndarray], float] = lambda array: float(np.sum(array ** 2))
genome = Genome(gene_low=-10.0, gene_high=10.0, dimension=10, rank=quadratic_rank)
algorithm_impl = GeneticAlgorithmImpl(genome=genome, population_size=20, best_last_generations_size=100)
# algorithm_impl.calculate()

linear_rank: Callable[[np.ndarray], float] = lambda array: float(np.sum(array))
genome2 = Genome(gene_low=0.0001, gene_high=1, dimension=1, rank=linear_rank)
algorithm_impl2 = GeneticAlgorithmImpl2(genome=genome2, population_size=1000, best_last_generations_size=10)
algorithm_impl2.calculate()
