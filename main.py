from genetic_algorithm.crossover import OnePointCrossover
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm
from genetic_algorithm.genome import QuadraticFunctionGenome
from genetic_algorithm.mutation import RandomMutation
from genetic_algorithm.parent_selection import TournamentSelection


class GeneticAlgorithmImpl(GeneticAlgorithm):

    def select_parents(self, fitness):
        return TournamentSelection().select_parents(self.population, fitness)

    def crossover(self, parents):
        return OnePointCrossover().crossover(parents)

    def mutate(self, crossovers):
        return RandomMutation().mutate(crossovers)


genome = QuadraticFunctionGenome(10)
algorithm_impl = GeneticAlgorithmImpl(genome=genome, population_size=20, gene_low=-10.0, gene_high=10.0,
                                      best_last_generations_size=100)
algorithm_impl.calculate()
