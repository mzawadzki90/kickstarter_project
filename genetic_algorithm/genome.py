from collections.abc import Iterable
from typing import Callable

from genetic_algorithm.gene import Gene


class Genome:
    genes: Iterable[Gene]
    rank: Callable[[Iterable[Gene]], float]

    def __init__(self, genes: Iterable[Gene], rank: Callable[[Iterable[Gene]], float]):
        self.genes = genes
        self.rank = rank

    def rank(self) -> float:
        return self.rank(self.genes)
