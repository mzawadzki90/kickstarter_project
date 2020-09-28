import numpy as np


class OnePointCrossover:

    def crossover(self, parents):
        parent1 = parents[0]
        parent2 = parents[1]
        crossover_point = self.select_crossover_point(parent1.size)
        crossover1 = np.append(parent1[0:crossover_point], parent2[crossover_point:])
        crossover2 = np.append(parent2[0:crossover_point], parent1[crossover_point:])
        return np.array([crossover1, crossover2])

    @staticmethod
    def select_crossover_point(size):
        if size % 2 == 0:
            return int(size / 2)
        else:
            return int(size / 2 + 1)
