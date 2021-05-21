from random import random, randint

import numpy as np

from utils.math import MathUtil


class Mutation:
    def mutate(self, crossovers: np.ndarray) -> np.ndarray:
        mutate1 = self.get_mutate(crossovers[0])
        mutate2 = self.get_mutate(crossovers[1])
        return np.array([mutate1, mutate2])

    def get_mutate(self, crossover: np.ndarray) -> np.ndarray:
        pass


class RandomMutation(Mutation):

    def get_mutate(self, crossover: np.ndarray) -> np.ndarray:
        mutate = np.copy(crossover)
        mutation_position = randint(0, crossover.size - 1)
        mutate[mutation_position] = random() * 10
        return mutate


class SwapMutation(Mutation):

    def get_mutate(self, crossover: np.ndarray) -> np.ndarray:
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


class FlipBitMutation(Mutation):

    def get_mutate(self, crossover: np.ndarray) -> np.ndarray:
        mutate = crossover[0]
        mutate_bitfield = MathUtil.float_to_bitfield(mutate)
        flip_position = randint(int(mutate_bitfield.size * 0.5), mutate_bitfield.size - 1)
        mutate_bitfield = MathUtil.flip_bit(mutate_bitfield, flip_position)
        mutate = MathUtil.bitfield_to_float(mutate_bitfield)
        return np.array([mutate])
