import numpy as np


class OnePointCrossover:

    # def as_dictionary(pair: Tuple[X, Y]) -> Dict[X, Y]:
    #   key, value = pair
    #   return {key: value}
    def crossover(self, parents):
        parent1 = parents[0]
        parent2 = parents[1]
        crossover_point = self.select_crossover_point(parent1.size)
        # use numpy concatenate or list or from collections import deque
        # add two list [1, 2, 3] + [4, 5, 6, 7]
        crossover1 = np.append(parent1[0:crossover_point], parent2[crossover_point:])
        crossover2 = np.append(parent2[0:crossover_point], parent1[crossover_point:])
        return np.array([crossover1, crossover2])

    @staticmethod
    def select_crossover_point(size):
        if size % 2 == 0:
            return int(size / 2)
        else:
            return int(size / 2 + 1)
