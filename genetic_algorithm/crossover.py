import copy
from typing import Sequence

from genetic_algorithm.genome import Genome
from utils.math import MathUtil


class Crossover:
    def crossover(self, parents: Sequence[Genome]) -> Sequence[Genome]:
        pass


def select_crossover_point(size: int) -> int:
    return MathUtil.random_int_from_range(1, size - 2)


class OnePointCrossover(Crossover):
    def crossover(self, parents: Sequence[Genome]) -> Sequence[Genome]:
        crossover1 = copy.deepcopy(parents[0])
        crossover2 = copy.deepcopy(parents[1])
        genes1 = crossover1.genes
        genes2 = crossover2.genes
        size = len(genes1)
        crossover_point = select_crossover_point(size)
        genes1_1 = genes1.select_range(0, crossover_point)
        genes1_2 = genes1.select_range(crossover_point, size)
        genes2_1 = genes2.select_range(0, crossover_point)
        genes2_2 = genes2.select_range(crossover_point, size)
        crossover1.genes = genes1_1 + genes2_2
        crossover2.genes = genes2_1 + genes1_2
        return [crossover1, crossover2]
