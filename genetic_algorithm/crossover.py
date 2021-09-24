import copy
from typing import Sequence

from genetic_algorithm.genome import Genome, LabeledSequence
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
        crossover1.genes = LabeledSequence()
        for x in range(0, crossover_point):
            crossover1.genes.append(genes1[x])
        for x in range(crossover_point, size):
            crossover1.genes.append(genes2[x])
        crossover2.genes = LabeledSequence()
        for x in range(0, crossover_point):
            crossover2.genes.append(genes2[x])
        for x in range(crossover_point, size):
            crossover2.genes.append(genes1[x])
        return [crossover1, crossover2]
