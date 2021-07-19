from abc import ABC
from typing import Callable, MutableSequence

from genetic_algorithm.gene import Gene


class LabeledSequence(MutableSequence[Gene], ABC):

    def get_by_label(self, label):
        return next((x for x in self if x.label == label), None)


class Genome:
    genes: LabeledSequence[Gene]
    rank_func: Callable[[LabeledSequence[Gene]], float]

    def __init__(self, genes: LabeledSequence[Gene], rank_funk: Callable[[LabeledSequence[Gene]], float]):
        self.genes = genes
        self.rank_func = rank_funk

    def rank(self) -> float:
        return self.rank_func(self.genes)
