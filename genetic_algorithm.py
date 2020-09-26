import numpy as np


class AbstractGeneticAlgorithm:

    def __init__(self, function_dimension, population_size):
        self.population = self.init_population(function_dimension, population_size)

    def calculate(self):
        population = self.population

    def select_parents(self):
        pass

    def crossover(self):
        pass

    def mutate(self):
        pass

    def select_survivor(self):
        pass

    @staticmethod
    def init_population(function_dimension, population_size):
        return np.random.uniform(low=0.0, high=10.0, size=(population_size, function_dimension))

    @staticmethod
    def calculate_population_fitness(population):
        return np.sum(population ** 2, axis=1)
