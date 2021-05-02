from typing import Callable

import numpy as np


class Genome:
    dimension: int
    rank: Callable[[np.ndarray], float]

    def __init__(self, dimension: int, rank: Callable[[np.ndarray], float]):
        self.dimension = dimension
        self.rank = rank

    def rank(self, array: np.ndarray) -> float:
        return self.rank(array)
