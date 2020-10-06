import numpy as np


class Genome:
    dimension: int

    def __init__(self, dimension: int):
        self.dimension = dimension

    def rank(self, array: np.ndarray) -> float:
        pass


class QuadraticFunctionGenome(Genome):
    def rank(self, array: np.ndarray) -> float:
        return float(np.sum(array ** 2))
