import csv
import os
import sys
from collections import deque
from datetime import datetime
from pathlib import Path
from typing import MutableSequence, Sequence
from typing import TextIO

import numpy as np

from genetic_algorithm.genome import Genome


def calculate_population_fitness(population: MutableSequence[Genome]) -> np.ndarray:
    return np.array([genome.rank() for genome in population])


class GeneticAlgorithm:
    genome: Genome
    population_size: int
    generation_count: int
    population_fitness: np.ndarray
    best_last_generations_size: int
    best_last_generations: deque
    worst_last_generations_size: int
    worst_last_generations: deque
    worst_from_previous_generations: float
    population: MutableSequence[Genome]
    stats_header: list = ['Generation number', 'Best fitness', 'Best genome', 'Worst fitness', 'Worst genome', 'Mean',
                          'Average', 'Standard deviation']
    stats_file_dir_str: str
    stats_file_dir_full: bool
    stats_file_base_name: str = 'genetic_algorithm_stats'
    stats_file: TextIO

    def __init__(self, genome: Genome, population_size: int = 10, generation_count: int = 100,
                 best_last_generations_size: int = 5, worst_last_generations_size: int = 5,
                 stats_file_dir_str: str = 'genetic_algorithm\\out\\stats', stats_file_dir_full=False):
        self.genome = genome
        self.stats_file_dir_str = stats_file_dir_str
        self.stats_file_dir_full = stats_file_dir_full
        self.population_size = population_size
        self.generation_count = generation_count
        self.best_last_generations_size = best_last_generations_size
        self.worst_last_generations_size = worst_last_generations_size
        self.worst_from_previous_generations = sys.float_info.max
        self.population = self.init_population()
        self.population_fitness = calculate_population_fitness(self.population)
        self.best_last_generations = deque(maxlen=self.best_last_generations_size)
        self.worst_last_generations = deque(maxlen=self.worst_last_generations_size)
        self.stats_file = self.__get_reference_or_create_file()
        self.__write_stats_header()

    def calculate(self) -> Genome:
        self.__save_best_for_generation()
        self.__save_worst_for_generation()
        generation_counter = 0
        while not self.__post_condition(generation_counter):
            self.__save_generation_stats(generation_counter)
            parents = self.select_parents(self.population_fitness, self.worst_from_previous_generations)
            crossovers = self.crossover(parents)
            mutates = self.mutate(crossovers)
            offsprings = self.select_survivor(mutates)
            self.__replace_worst_elements(offsprings, generation_counter)
            self.__save_best_for_generation()
            self.__save_worst_for_generation()
            generation_counter += 1
        self.stats_file.close()
        return self.__get_best()

    def init_population(self) -> MutableSequence[Genome]:
        pass

    def select_parents(self, fitness: np.ndarray, worst_from_previous_generations: float) -> Sequence[Genome]:
        pass

    def crossover(self, parents: Sequence[Genome]) -> Sequence[Genome]:
        pass

    def mutate(self, crossovers: Sequence[Genome]) -> Sequence[Genome]:
        pass

    def select_survivor(self, mutates: Sequence[Genome]) -> Sequence[Genome]:
        pass

    def __get_reference_or_create_file(self) -> TextIO:
        now = datetime.utcnow()
        date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = self.stats_file_base_name + '_' + date_time + '.csv'
        if self.stats_file_dir_full:
            dir_path = Path(self.stats_file_dir_str)
            dir_path.mkdir(parents=True, exist_ok=True)
            file_path_str = os.path.join(self.stats_file_dir_str, file_name)
        else:
            current_dir = os.getcwd()
            dir_path = Path(os.path.join(current_dir, self.stats_file_dir_str))
            dir_path.mkdir(parents=True, exist_ok=True)
            file_path_str = os.path.join(current_dir, self.stats_file_dir_str, file_name)
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

    def __save_worst_for_generation(self):
        if len(self.worst_last_generations) == self.worst_last_generations_size:
            self.worst_last_generations.popleft()
        self.worst_last_generations.append(self.population[self.population_fitness.argmax()])
        self.worst_from_previous_generations = max(self.worst_last_generations, key=lambda g: g.fitness).fitness

    def __save_generation_stats(self, generation_counter):
        best_fitness = self.population_fitness[self.population_fitness.argmin()]
        best_genome = self.population[self.population_fitness.argmin()]
        worst_fitness = self.population_fitness[self.population_fitness.argmax()]
        worst_genome = self.population[self.population_fitness.argmax()]
        mean = np.mean(self.population_fitness)
        average = np.average(self.population_fitness)
        standard_deviation = np.std(self.population_fitness)
        csv.writer(self.stats_file).writerow(
            [generation_counter, best_fitness, best_genome, worst_fitness, worst_genome, mean, average,
             standard_deviation])

    def __post_condition(self, generation_counter: int) -> bool:
        return generation_counter > self.generation_count

    def __replace_worst_elements(self, offsprings: Sequence[Genome], counter: int):
        worst_indices_size = len(offsprings)
        worst_indices = np.argpartition(self.population_fitness, -worst_indices_size)[-worst_indices_size:]
        for i in range(0, worst_indices_size):
            self.population[worst_indices[i]] = offsprings[i]
            self.population_fitness[worst_indices[i]] = offsprings[i].fitness
        print("Generation: ", counter, "; Current population: ")
        for genome in self.population:
            print(genome)

    def __get_best(self) -> Genome:
        best = min(self.best_last_generations, key=lambda g: g.fitness)
        print("Best: ", best)
        print("Best score: ", best.fitness)
        return best
