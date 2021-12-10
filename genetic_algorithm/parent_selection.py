import copy
from typing import MutableSequence, Sequence

import numpy as np

from genetic_algorithm.genome import Genome


class ParentSelection:
    def select_parents(self, population: MutableSequence[Genome], fitness: np.ndarray,
                       worst_from_previous_generations: float) -> Sequence[Genome]:
        pass


class TournamentSelection(ParentSelection):
    def select_parents(self, population: MutableSequence[Genome], fitness: np.ndarray,
                       worst_from_previous_generations: float) -> Sequence[Genome]:
        population_copy = copy.deepcopy(population)
        fitness_copy = np.copy(fitness)
        parent1, index1 = self.__select_parent(population_copy, fitness_copy, worst_from_previous_generations)
        del population_copy[index1]
        fitness_copy = np.delete(fitness_copy, index1)
        parent2, index2 = self.__select_parent(population_copy, fitness_copy, worst_from_previous_generations)
        return [parent1, parent2]

    def __select_parent(self, population: MutableSequence[Genome], fitness: np.ndarray,
                        worst_from_previous_generations: float) -> [Genome, int]:
        population_rows = len(population)
        probability_arr = self.__get_probability_arr(fitness, worst_from_previous_generations)
        candidate_index = np.random.choice(a=population_rows, size=1,
                                           p=probability_arr)[0]
        return population[candidate_index], candidate_index

    def __get_probability_arr(self, fitness: np.ndarray, worst_from_previous_generations: float) -> iter:
        fitness_rows = fitness.shape[0]
        if fitness_rows == 1:
            return np.array([1])
        if fitness.std() < 0.001:
            return np.ones(fitness_rows) / fitness_rows
        fitness_sum = np.sum(fitness)
        reshaped = (worst_from_previous_generations - fitness) / (
                (fitness_rows * worst_from_previous_generations) - fitness_sum)
        return reshaped.tolist()
