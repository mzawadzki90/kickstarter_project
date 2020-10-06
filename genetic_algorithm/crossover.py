import numpy as np


class Crossover:
    def crossover(self, parents: np.ndarray) -> np.ndarray:
        pass


class OnePointCrossover(Crossover):
    def crossover(self, parents: np.ndarray) -> np.ndarray:
        parent1 = parents[0]
        parent2 = parents[1]
        crossover_point = self.select_crossover_point(parent1.size)
        crossover1 = np.concatenate((parent1[0:crossover_point], parent2[crossover_point:]))
        crossover2 = np.concatenate((parent2[0:crossover_point], parent1[crossover_point:]))
        return np.array([crossover1, crossover2])

    def select_crossover_point(self, size: int) -> int:
        if size % 2 == 0:
            return int(size / 2)
        else:
            return int(size / 2 + 1)
