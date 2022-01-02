import copy
from typing import MutableSequence, Sequence

import numpy as np

from genetic_algorithm.genome import Genome


def get_probability_arr(fitness: np.ndarray, worst_from_previous_generations: float) -> iter:
    fitness_copy = copy.deepcopy(fitness)
    fitness_rows = fitness_copy.shape[0]
    if fitness_rows == 1:
        return np.array([1])
    if fitness_copy.std() < 0.001:
        return np.ones(fitness_rows) / fitness_rows
    fitness_copy[fitness_copy == 0.] = 10 ** -8
    fitness_copy = np.power(fitness_copy, -1)
    worst_from_previous_generations = np.power(worst_from_previous_generations, -1)
    fitness_sum = np.sum(np.abs(fitness_copy - worst_from_previous_generations))
    reshaped = np.abs(fitness_copy - worst_from_previous_generations) / fitness_sum
    return reshaped.tolist()


class ParentSelection:
    def select_parents(self, population: MutableSequence[Genome], fitness: np.ndarray,
                       worst_from_previous_generations: float) -> Sequence[Genome]:
        pass


class TournamentSelection(ParentSelection):
    def select_parents(self, population: MutableSequence[Genome], fitness: np.ndarray,
                       worst_from_previous_generations: float) -> Sequence[Genome]:
        population_rows = len(population)
        probability_arr = get_probability_arr(fitness, worst_from_previous_generations)
        candidate_index1, candidate_index2 = np.random.choice(a=population_rows, size=2,
                                                              p=probability_arr).tolist()
        return [population[candidate_index1], population[candidate_index2]]
