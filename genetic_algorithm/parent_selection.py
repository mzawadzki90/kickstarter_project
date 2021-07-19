import copy
from collections import MutableSequence, Sequence

import numpy as np

from genetic_algorithm.genome import Genome


class ParentSelection:
    def select_parents(self, population: MutableSequence[Genome], fitness: np.ndarray) -> Sequence[Genome]:
        pass


class TournamentSelection(ParentSelection):
    def select_parents(self, population: MutableSequence[Genome], fitness: np.ndarray) -> Sequence[Genome]:
        population_copy = copy.deepcopy(population)
        fitness_copy = np.copy(fitness)
        parent1, index1 = self.__select_parent(population_copy, fitness_copy)
        del population_copy[index1]
        fitness_copy = np.delete(fitness_copy, index1)
        parent2, index2 = self.__select_parent(population_copy, fitness_copy)
        return [parent1, parent2]

    def __select_parent(self, population: MutableSequence[Genome], fitness: np.ndarray) -> [Genome, int]:
        population_rows = len(population)
        candidates = np.random.choice(a=population_rows, size=self.__get_candidates_size(population_rows),
                                      p=self.__get_probability_arr(fitness))
        candidates_fitness = fitness[candidates]
        min_candidate_index = np.where(fitness == np.min(candidates_fitness))
        return population[min_candidate_index[0][0]], min_candidate_index[0][0]

    def __get_probability_arr(self, fitness: np.ndarray) -> iter:
        fitness_rows = fitness.shape[0]
        if fitness_rows == 1:
            return np.array([1])

        if fitness.std() < 0.001:
            return np.ones(fitness_rows) / fitness_rows

        max_fitness = np.max(fitness)
        fitness_sum = np.sum(fitness)
        reshaped = (max_fitness - fitness) / ((fitness_rows * max_fitness) - fitness_sum)

        return reshaped.tolist()

    def __get_candidates_size(self, population_rows: int) -> int:
        return max(2, int(population_rows * 0.3))
