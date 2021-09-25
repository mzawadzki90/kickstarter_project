from collections import deque
from typing import MutableSequence, Sequence

import numpy as np

from genetic_algorithm.genome import Genome


class GeneticAlgorithm:
    genome: Genome
    population_size: int
    generation_count: int
    population_fitness: np.ndarray
    best_last_generations_size: int
    population: MutableSequence[Genome]
    best_last_generations: deque

    def __init__(self, genome: Genome, population_size: int = 10, generation_count: int = 100,
                 best_last_generations_size: int = 5):
        self.genome = genome
        self.population_size = population_size
        self.generation_count = generation_count
        self.best_last_generations_size = best_last_generations_size
        self.population = self.init_population()
        self.population_fitness = self.__calculate_population_fitness(self.population)
        self.best_last_generations = deque(maxlen=self.best_last_generations_size)

    def calculate(self) -> Genome:
        self.__save_best_for_generation()
        generation_counter = 1
        while not self.__post_condition(generation_counter):
            parents = self.select_parents(self.population_fitness)
            crossovers = self.crossover(parents)
            mutates = self.mutate(crossovers)
            offspring = self.__select_survivor(mutates)
            generation_counter += 1
            self.__replace_worst_element(offspring, generation_counter)
            self.__save_best_for_generation()
        return self.__get_best()

    def init_population(self) -> MutableSequence[Genome]:
        pass

    def select_parents(self, fitness: np.ndarray) -> Sequence[Genome]:
        pass

    def crossover(self, parents: Sequence[Genome]) -> Sequence[Genome]:
        pass

    def mutate(self, crossovers: Sequence[Genome]) -> Sequence[Genome]:
        pass

    def __save_best_for_generation(self):
        if len(self.best_last_generations) == self.best_last_generations_size:
            self.best_last_generations.popleft()
        self.best_last_generations.append(self.population[self.population_fitness.argmin()])
        print("The best from the last ", self.best_last_generations_size, " generations:")
        for genome in self.best_last_generations:
            print(genome)

    def __post_condition(self, generation_counter: int) -> bool:
        return generation_counter >= self.generation_count

    def __select_survivor(self, mutates: Sequence[Genome]) -> Genome:
        mutate1 = mutates[0]
        mutate2 = mutates[1]
        if mutate1.rank() <= mutate2.rank():
            return mutate1
        else:
            return mutate2

    def __replace_worst_element(self, offspring: Genome, counter: int):
        worst_index = self.population_fitness.argmax()
        self.population[worst_index] = offspring
        self.population_fitness[worst_index] = offspring.fitness
        print("Generation: ", counter, "; Current population: ")
        for genome in self.population:
            print(genome)

    def __get_best(self) -> Genome:
        best = min(self.best_last_generations, key=lambda g: g.fitness)
        print("Best: ", best)
        print("Best score: ", best.fitness)
        return best

    def __calculate_population_fitness(self, population: MutableSequence[Genome]) -> np.ndarray:
        fitness_arr = []
        for genome in population:
            fitness_arr.append(genome.rank())
        return np.array(fitness_arr)
