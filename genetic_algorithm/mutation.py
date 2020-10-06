from random import random, randint

import numpy as np


class Mutation:
    def mutate(self, crossovers: np.ndarray) -> np.ndarray:
        pass


class RandomMutation(Mutation):
    def mutate(self, crossovers: np.ndarray) -> np.ndarray:
        mutate1 = self.__get_mutate(crossovers[0])
        mutate2 = self.__get_mutate(crossovers[1])
        return np.array([mutate1, mutate2])

    def __get_mutate(self, crossover: np.ndarray) -> np.ndarray:
        mutate = np.copy(crossover)
        mutate[randint(0, crossover.size - 1)] = random() * 10
        return mutate


class SwapMutation(Mutation):
    def mutate(self, crossovers: np.ndarray) -> np.ndarray:
        mutate1 = self.__get_mutate(crossovers[0])
        mutate2 = self.__get_mutate(crossovers[1])
        return np.array([mutate1, mutate2])

    def __get_mutate(self, crossover: np.ndarray) -> np.ndarray:
        mutate = np.copy(crossover)
        swap_point, opposite_swap = self.__get_swap_points(crossover.size)
        mutate[swap_point], mutate[opposite_swap] = mutate[opposite_swap], mutate[swap_point]
        return mutate

    def __get_swap_points(self, size: int) -> [int, int]:
        swap_point = int(random() * size)
        if swap_point > (size - 1) / 2:
            opposite_swap = -1 - swap_point
        else:
            opposite_swap = size - swap_point - 1
        return swap_point, opposite_swap
