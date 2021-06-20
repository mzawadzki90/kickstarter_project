import copy
from collections import Sequence

from genetic_algorithm.genome import Genome


class Crossover:
    def crossover(self, parents: Sequence[Genome]) -> Sequence[Genome]:
        pass


def select_crossover_point(size: int) -> int:
    if size % 2 == 0:
        return int(size / 2)
    else:
        return int(size / 2 + 1)


class OnePointCrossover(Crossover):
    def crossover(self, parents: Sequence[Genome]) -> Sequence[Genome]:
        crossover1 = copy.deepcopy(parents[0])
        crossover2 = copy.deepcopy(parents[1])
        genes1 = crossover1.genes
        genes2 = crossover2.genes
        size = len(genes1)
        crossover_point = select_crossover_point(size)
        crossover1.genes = list(genes1[0:crossover_point]) + list(genes2[crossover_point:])
        crossover2.genes = list(genes2[0:crossover_point]) + list(genes1[crossover_point:])
        return [crossover1, crossover2]
