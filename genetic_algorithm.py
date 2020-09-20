import numpy as np


class AbstractGeneticAlgorithm:

    def __init__(self, function_dimension, population_size):
        self.population = self.init_population(function_dimension, population_size)

    @staticmethod
    def init_population(function_dimension, population_size):
        return np.random.randn(population_size, function_dimension)

    @staticmethod
    def calculate_fitness(chromosome):
        return np.sum(chromosome ** 2)

    def calculate(self):
        population = self.population
        # TODO: add rest of implementation

    def select_parents(self):
        pass

    def crossover(self):
        pass

    def mutate(self):
        pass

    def select_survivor(self):
        pass
