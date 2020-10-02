import numpy as np


# not abstract
class AbstractGeneticAlgorithm:

    # class QuadraticFunctionGenome(Genome):
    #     _parameters: np.ndarray
    #
    #     def init(self, dimensions: int):
    #         self._parameters = np.random.random(dimensions)
    #
    #     def rank(self) -> float:
    #         return ...
    #
    # # ===
    #
    # def rank(genome: QuadraticFunctionGenome) -> float:
    #     return ...

    def __init__(self, function_dimension, population_size):
        self.function_dimension = function_dimension
        self.population_size = population_size
        self.population = self.init_population()
        self.best_hundred_last_generations = np.ones(shape=(100, function_dimension))

    def calculate(self):
        fitness = self.calculate_population_fitness(self.population)
        self.save_best_for_generation(fitness)
        generation_counter = 1
        while not self.post_condition():
            parents = self.select_parents(fitness)
            crossovers = self.crossover(parents)
            mutates = self.mutate(crossovers)
            offspring = self.select_survivor(mutates)
            generation_counter += 1
            self.replace_worst_element(offspring, fitness, generation_counter)
            fitness = self.calculate_population_fitness(self.population)
            self.save_best_for_generation(fitness)
        return self.get_best()

    def save_best_for_generation(self, fitness):
        self.best_hundred_last_generations = np.roll(self.best_hundred_last_generations, 1, axis=0)
        self.best_hundred_last_generations[0] = self.population[fitness.argmin()]
        print("The best from the last 100 generations:", self.best_hundred_last_generations)

    # add to separete file
    def post_condition(self):
        best_hundred_last_generations_fitness = self.calculate_population_fitness(self.best_hundred_last_generations)
        return best_hundred_last_generations_fitness.std() < 0.01 or np.min(best_hundred_last_generations_fitness) == 0

    def select_parents(self, fitness):
        pass

    def crossover(self, parents):
        pass

    def mutate(self, crossovers):
        pass

    # add to separete file
    def select_survivor(self, mutates):
        mutate1 = mutates[0]
        mutate2 = mutates[1]
        return np.where(self.calculate_fitness(mutate1) > self.calculate_fitness(mutate2), mutate2, mutate1)

    def replace_worst_element(self, offspring, fitness, counter):
        self.population[fitness.argmax()] = offspring
        print("Generation: ", counter, "; Current population: ", self.population)

    def get_best(self):
        return np.min(np.sum(self.best_hundred_last_generations ** 2, axis=1))

    def init_population(self):
        population = np.random.uniform(low=0.0, high=10.0, size=(self.population_size, self.function_dimension))
        print("Generation: 1; Population: ", population)
        return population

    # not static
    @staticmethod
    def calculate_population_fitness(population):
        return np.sum(population ** 2, axis=1)

    # public
    # _  # protected
    # __  # private
    @staticmethod
    def calculate_fitness(chromosome):
        return np.sum(chromosome ** 2)
