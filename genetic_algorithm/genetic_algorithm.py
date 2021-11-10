import csv
import os
from collections import deque
from pathlib import Path
from typing import MutableSequence, Sequence
from typing import TextIO

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
    stats_header: list = ['Generation number', 'Best', 'Worst', 'Mean', 'Average', 'Standard deviation']
    stats_file_dir_str: str
    stats_file_name: str = 'genetic_algorithm_stats.csv'
    stats_file: TextIO

    def __init__(self, genome: Genome, population_size: int = 10, generation_count: int = 100,
                 best_last_generations_size: int = 5,
                 stats_file_dir_str: str = 'C:\\Users\\micha\\Praca inżynierska PJATK\\kickstarter\\genetic_algorithm\\out\\stats'):
        self.genome = genome
        self.stats_file_dir_str = stats_file_dir_str
        self.population_size = population_size
        self.generation_count = generation_count
        self.best_last_generations_size = best_last_generations_size
        self.population = self.init_population()
        self.population_fitness = self.__calculate_population_fitness(self.population)
        self.best_last_generations = deque(maxlen=self.best_last_generations_size)
        self.stats_file = self.__get_reference_or_create_file()
        self.__write_stats_header()

    def calculate(self) -> Genome:
        self.__save_best_for_generation()
        generation_counter = 0
        while not self.__post_condition(generation_counter):
            self.__save_generation_stats(generation_counter)
            parents = self.select_parents(self.population_fitness)
            crossovers = self.crossover(parents)
            mutates = self.mutate(crossovers)
            offspring = self.__select_survivor(mutates)
            self.__replace_worst_element(offspring, generation_counter)
            self.__save_best_for_generation()
            generation_counter += 1
        self.stats_file.close()
        return self.__get_best()

    def init_population(self) -> MutableSequence[Genome]:
        pass

    def select_parents(self, fitness: np.ndarray) -> Sequence[Genome]:
        pass

    def crossover(self, parents: Sequence[Genome]) -> Sequence[Genome]:
        pass

    def mutate(self, crossovers: Sequence[Genome]) -> Sequence[Genome]:
        pass

    def __calculate_population_fitness(self, population: MutableSequence[Genome]) -> np.ndarray:
        fitness_arr = []
        for genome in population:
            fitness_arr.append(genome.rank())
        return np.array(fitness_arr)

    def __get_reference_or_create_file(self) -> TextIO:
        dir_path = Path(self.stats_file_dir_str)
        dir_path.mkdir(parents=True, exist_ok=True)
        file_path_str = os.path.join(self.stats_file_dir_str, self.stats_file_name)
        file_path = Path(file_path_str)
        file_path.touch(exist_ok=True)
        return open(file=file_path_str, mode='w')

    def __write_stats_header(self):
        writer = csv.writer(self.stats_file)
        writer.writerow(self.stats_header)

    def __save_best_for_generation(self):
        if len(self.best_last_generations) == self.best_last_generations_size:
            self.best_last_generations.popleft()
        self.best_last_generations.append(self.population[self.population_fitness.argmin()])
        print("The best from the last ", self.best_last_generations_size, " generations:")
        for genome in self.best_last_generations:
            print(genome)

    def __save_generation_stats(self, generation_counter):
        best = self.population_fitness[self.population_fitness.argmin()]
        worst = self.population_fitness[self.population_fitness.argmax()]
        mean = np.mean(self.population_fitness)
        average = np.mean(self.population_fitness)
        standard_deviation = np.std(self.population_fitness)
        csv.writer(self.stats_file).writerow(
            [generation_counter, best, worst, mean, average, standard_deviation])

    def __post_condition(self, generation_counter: int) -> bool:
        return generation_counter > self.generation_count

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
