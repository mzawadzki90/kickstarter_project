from typing import Sequence

import numpy as np

from genetic_algorithm.genome import Genome
from utils.math import MathUtil


class Crossover:
    def crossover(self, parents: Sequence[Genome]) -> Sequence[Genome]:
        pass


def select_crossover_point(size: int) -> int:
    return MathUtil.random_int_from_range(1, size - 2)


def select_two_crossover_points(genome_size: int) -> [int]:
    points = np.random.choice(a=range(1, genome_size - 1), replace=False, size=2).tolist()
    points.sort()
    return points


class OnePointCrossover(Crossover):
    def crossover(self, parents: Sequence[Genome]) -> Sequence[Genome]:
        genes1 = parents[0].genes
        genes2 = parents[1].genes
        genome_size = len(genes1)
        crossover_point = select_crossover_point(genome_size)
        genes1_1 = genes1.select_range(0, crossover_point)
        genes1_2 = genes1.select_range(crossover_point, genome_size)
        genes2_1 = genes2.select_range(0, crossover_point)
        genes2_2 = genes2.select_range(crossover_point, genome_size)
        rank_func = parents[0].rank_func
        crossover1 = Genome(genes=genes1_1 + genes2_2, rank_funk=rank_func)
        crossover2 = Genome(genes=genes2_1 + genes1_2, rank_funk=rank_func)
        return [crossover1, crossover2]


class TwoPointsCrossover(Crossover):
    def crossover(self, parents: Sequence[Genome]) -> Sequence[Genome]:
        genes1 = parents[0].genes
        genes2 = parents[1].genes
        genome_size = len(genes1)
        crossover_point1, crossover_point2 = select_two_crossover_points(genome_size)
        genes1_1 = genes1.select_range(0, crossover_point1)
        genes1_2 = genes1.select_range(crossover_point1, crossover_point2)
        genes1_3 = genes1.select_range(crossover_point2, genome_size)
        genes2_1 = genes2.select_range(0, crossover_point1)
        genes2_2 = genes2.select_range(crossover_point1, crossover_point2)
        genes2_3 = genes2.select_range(crossover_point2, genome_size)
        rank_func = parents[0].rank_func
        crossover1 = Genome(genes=genes2_1 + genes1_2 + genes2_3, rank_funk=rank_func)
        crossover2 = Genome(genes=genes1_1 + genes2_2 + genes1_3, rank_funk=rank_func)
        crossover3 = Genome(genes=genes1_1 + genes2_2 + genes2_3, rank_funk=rank_func)
        crossover4 = Genome(genes=genes1_1 + genes1_2 + genes2_3, rank_funk=rank_func)
        crossover5 = Genome(genes=genes2_1 + genes1_2 + genes1_3, rank_funk=rank_func)
        crossover6 = Genome(genes=genes2_1 + genes2_2 + genes1_3, rank_funk=rank_func)
        return [crossover1, crossover2, crossover3, crossover4, crossover5, crossover6]
