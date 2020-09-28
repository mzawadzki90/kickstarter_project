from random import random

import numpy as np


class SwapMutation:

    def mutate(self, crossovers):
        mutate1 = self.get_mutate(crossovers[0])
        mutate2 = self.get_mutate(crossovers[1])
        return np.array([mutate1, mutate2])

    def get_mutate(self, crossover):
        mutate = np.copy(crossover)
        swap_point, opposite_swap = self.get_swap_points(crossover.size)
        mutate[swap_point], mutate[opposite_swap] = mutate[opposite_swap], mutate[swap_point]
        return mutate

    @staticmethod
    def get_swap_points(size):
        swap_point = int(random() * size)
        if swap_point > (size - 1) / 2:
            opposite_swap = -1 - swap_point
        else:
            opposite_swap = size - swap_point - 1
        return swap_point, opposite_swap
