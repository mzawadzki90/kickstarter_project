from random import random, randint

import numpy as np


class RandomMutation:

    def mutate(self, crossovers):
        mutate1 = self.get_mutate(crossovers[0])
        mutate2 = self.get_mutate(crossovers[1])
        return np.array([mutate1, mutate2])

    @staticmethod
    def get_mutate(crossover):
        mutate = np.copy(crossover)
        mutate[randint(0, crossover.size - 1)] = random() * 10
        return mutate
