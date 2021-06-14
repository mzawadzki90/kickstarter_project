from collections.abc import Sequence
from typing import Callable

from genetic_algorithm.gene import Gene


class Genome:
    genes: Sequence[Gene]
    rank_func: Callable[[Sequence[Gene]], float]

    def __init__(self, genes: Sequence[Gene], rank: Callable[[Sequence[Gene]], float]):
        self.genes = genes
        self.rank_func = rank

    def rank(self) -> float:
        return self.rank_func(self.genes)
