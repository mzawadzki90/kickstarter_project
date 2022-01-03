from typing import Callable, MutableSequence, Generic, TypeVar

from genetic_algorithm.gene import Gene

T = TypeVar('T')


class LabeledSequence(MutableSequence[Gene], Generic[T]):

    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data

    def __add__(self, other):
        return LabeledSequence(self.data + other.data)

    def insert(self, index: int, value: T) -> None:
        self.data.insert(index, value)

    def __getitem__(self, i: int) -> T:
        if isinstance(i, slice):
            return self.__class__()
        else:
            return self.data[i]

    def __setitem__(self, i: int, o: T) -> None:
        self.data[i] = o

    def __delitem__(self, i: int) -> None:
        del self.data[i]

    def __len__(self) -> int:
        return len(self.data)

    def select_range(self, start: int, stop: int):
        return LabeledSequence(self.data[start:stop])

    def get_by_label(self, label):
        return next((x for x in self if x.label == label), None)


class Genome:
    genes: LabeledSequence[Gene]
    rank_func: Callable[[LabeledSequence[Gene]], float]
    fitness: float

    def __init__(self, genes: LabeledSequence[Gene], rank_funk: Callable[[LabeledSequence[Gene]], float]):
        self.genes = genes
        self.rank_func = rank_funk

    def rank(self) -> float:
        self.fitness = self.rank_func(self.genes)
        return self.fitness

    def __str__(self) -> str:
        string_representation = 'Genome{fitness:' + str(self.fitness) + ',genes:['
        for gene in self.genes:
            string_representation += gene.__str__()
            string_representation += ','
        string_representation += ']}'
        return string_representation
