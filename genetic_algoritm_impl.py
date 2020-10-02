from genetic_algorithm import AbstractGeneticAlgorithm
from one_point_crossover import OnePointCrossover
from random_mutation import RandomMutation
from tournament_selection import TournamentSelection


# remove
class GeneticAlgorithmImpl(AbstractGeneticAlgorithm):

    def select_parents(self, fitness):
        return TournamentSelection().select_parents(self.population, fitness)

    def crossover(self, parents):
        return OnePointCrossover().crossover(parents)

    def mutate(self, crossovers):
        return RandomMutation().mutate(crossovers)
