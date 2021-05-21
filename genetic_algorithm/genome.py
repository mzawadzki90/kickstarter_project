from typing import Callable

import numpy as np


class Genome:
    gene_low: float
    gene_high: float
    dimension: int
    rank: Callable[[np.ndarray], float]

    def __init__(self, gene_low: float, gene_high: float, dimension: int, rank: Callable[[np.ndarray], float]):
        self.gene_low = gene_low
        self.gene_high = gene_high
        self.dimension = dimension
        self.rank = rank

    def rank(self, array: np.ndarray) -> float:
        return self.rank(array)
