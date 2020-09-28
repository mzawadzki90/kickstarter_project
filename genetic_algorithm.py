import numpy as np


class AbstractGeneticAlgorithm:

    def __init__(self, function_dimension, population_size):
        self.population = self.init_population(function_dimension, population_size)
        self.best_three_last_generations = np.zeros(shape=(1, 3))

    def calculate(self):
        fitness = self.calculate_population_fitness()
        self.save_best_for_generation(fitness)
        while not self.post_condition():
            parent1, parent2 = self.select_parents(fitness)
            crossovers = self.crossover(parent1, parent2)
            mutates = self.mutate(crossovers)
            offspring = self.select_survivor(mutates)
            self.replace_worst_element(offspring, fitness)
            fitness = self.calculate_population_fitness()
            self.save_best_for_generation(fitness)
        return self.get_best()

    def calculate_population_fitness(self):
        fitness = np.sum(self.population ** 2, axis=1)
        return fitness

    def save_best_for_generation(self, fitness):
        self.best_three_last_generations[3] = self.best_three_last_generations[2]
        self.best_three_last_generations[2] = self.best_three_last_generations[1]
        self.best_three_last_generations[0] = self.population[fitness.argmin()[0]]

    def post_condition(self):
        return self.best_three_last_generations.std() < 0.005

    def select_parents(self, fitness):
        pass

    def crossover(self, parents):
        pass

    def mutate(self, crossovers):
        pass

    def select_survivor(self, mutates):
        pass

    def replace_worst_element(self, offspring, fitness):
        np.put(self.population, fitness.argmax()[0], offspring)

    def get_best(self):
        return np.min(self.best_three_last_generations)

    @staticmethod
    def init_population(function_dimension, population_size):
        return np.random.uniform(low=0.0, high=10.0, size=(population_size, function_dimension))
