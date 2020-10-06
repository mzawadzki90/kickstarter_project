import numpy as np

from genetic_algorithm.genome import Genome


class GeneticAlgorithm:
    genome: Genome
    population_size: int
    population: np.ndarray
    best_last_generations: np.ndarray

    def __init__(self, genome: Genome, population_size: int, gene_low: float = 0.0, gene_high: float = 10.0,
                 best_last_generations_size: int = 100):
        self.genome = genome
        self.population_size = population_size
        self.population = self.__init_population(gene_low, gene_high)
        self.best_last_generations_size = best_last_generations_size
        self.best_last_generations = np.ones(shape=(best_last_generations_size, genome.dimension))

    def calculate(self) -> float:
        fitness = self.__calculate_population_fitness(self.population)
        self.__save_best_for_generation(fitness)
        generation_counter = 1
        while not self.__post_condition():
            parents = self.select_parents(fitness)
            crossovers = self.crossover(parents)
            mutates = self.mutate(crossovers)
            offspring = self.__select_survivor(mutates)
            generation_counter += 1
            self.__replace_worst_element(offspring, fitness, generation_counter)
            fitness = self.__calculate_population_fitness(self.population)
            self.__save_best_for_generation(fitness)
        return self.__get_best()

    def select_parents(self, fitness: np.ndarray) -> np.ndarray:
        pass

    def crossover(self, parents: np.ndarray) -> np.ndarray:
        pass

    def mutate(self, crossovers: np.ndarray) -> np.ndarray:
        pass

    def __save_best_for_generation(self, fitness: np.ndarray):
        self.best_last_generations = np.roll(self.best_last_generations, 1, axis=0)
        self.best_last_generations[0] = self.population[fitness.argmin()]
        print("The best from the last ", self.best_last_generations_size, " generations:", self.best_last_generations)

    def __post_condition(self) -> bool:
        best_hundred_last_generations_fitness = self.__calculate_population_fitness(self.best_last_generations)
        return best_hundred_last_generations_fitness.std() < 0.05 or np.min(best_hundred_last_generations_fitness) == 0

    def __select_survivor(self, mutates: np.ndarray) -> np.ndarray:
        mutate1 = mutates[0]
        mutate2 = mutates[1]
        return np.where(self.__calculate_fitness(mutate1) > self.__calculate_fitness(mutate2), mutate2, mutate1)

    def __replace_worst_element(self, offspring: np.ndarray, fitness: np.ndarray, counter: int):
        self.population[fitness.argmax()] = offspring
        print("Generation: ", counter, "; Current population: ", self.population)

    def __get_best(self) -> float:
        return np.min(np.sum(self.best_last_generations ** 2, axis=1))

    def __init_population(self, low: float, high: float):
        population = np.random.uniform(low=low, high=high, size=(self.population_size, self.genome.dimension))
        print("Generation: 1; Population: ", population)
        return population

    def __calculate_population_fitness(self, population: np.ndarray) -> np.ndarray:
        return np.apply_along_axis(self.genome.rank, axis=1, arr=population)

    def __calculate_fitness(self, chromosome: np.ndarray) -> float:
        return self.genome.rank(chromosome)
