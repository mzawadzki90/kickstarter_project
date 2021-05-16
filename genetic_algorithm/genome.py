from typing import Callable

import numpy as np


class Genome:
    dimension: int
    rank: Callable[[np.ndarray], float]
    convert_to_binary: bool

    def __init__(self, dimension: int, rank: Callable[[np.ndarray], float], convert_to_binary: bool):
        self.dimension = dimension
        self.rank = rank
        self.convert_to_binary = convert_to_binary

    def rank(self, array: np.ndarray) -> float:
        return self.rank(array)
