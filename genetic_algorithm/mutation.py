import copy
from typing import Union, Sequence

import numpy as np

from genetic_algorithm.gene import Gene, IntegerGene, FloatGene
from genetic_algorithm.genome import Genome
from utils.math import MathUtil

numeric = Union[int, float]


def crop_to_boundaries(mutate_gene: Gene, mutate_value: numeric) -> numeric:
    maximum = mutate_gene.maximum
    if mutate_value > maximum:
        mutate_value = maximum
    minimum = mutate_gene.minimum
    if mutate_value < minimum:
        mutate_value = minimum
    return mutate_value


def max_min_delta(mutate_gene: Gene) -> Sequence[numeric]:
    max_val = abs((mutate_gene.maximum - mutate_gene.minimum) / 2)
    min_val = -max_val
    return max_val, min_val


def select_mutation_points(start_point: int, stop_point: int, amount: int) -> [int]:
    points = np.random.choice(a=range(start_point, stop_point), replace=False, size=amount).tolist()
    points.sort()
    return points


class Mutation:
    def mutate(self, crossovers: Sequence[Genome]) -> Sequence[Genome]:
        mutates = []
        for crossover in crossovers:
            mutates.append(self.get_mutate(crossover))
        return mutates

    def get_mutate(self, crossover: Genome) -> Genome:
        mutate = copy.deepcopy(crossover)
        genome_size = len(crossover.genes)
        mutation_positions = select_mutation_points(start_point=0,
                                                    stop_point=genome_size,
                                                    amount=int(genome_size / 3))
        for position in mutation_positions:
            mutate.genes[position] = self.__get_mutate_gene(crossover.genes[position])
        # recalculate fitness for mutate
        mutate.rank()
        return mutate

    def __get_mutate_gene(self, gene: Gene) -> Gene:
        if isinstance(gene, IntegerGene):
            return self.mutate_integer_gene(gene)
        elif isinstance(gene, FloatGene):
            return self.mutate_float_gene(gene)

    def mutate_integer_gene(self, gene: IntegerGene) -> IntegerGene:
        pass

    def mutate_float_gene(self, gene: FloatGene) -> FloatGene:
        pass


class FlipBitMutation(Mutation):

    def mutate_integer_gene(self, gene: IntegerGene) -> IntegerGene:
        mutate_gene = copy.deepcopy(gene)
        bitfield = MathUtil.integer_to_bitfield(mutate_gene.value)
        bitfield_size = bitfield.size
        flip_position = MathUtil.random_int_from_range(min_val=int(bitfield_size * (1 / 10)), max_val=bitfield_size - 1)
        mutate_bitfield = MathUtil.flip_bit(bitfield=bitfield, pos=flip_position)
        mutate_value = MathUtil.bitfield_to_integer(mutate_bitfield)
        mutate_value = crop_to_boundaries(mutate_gene, mutate_value)
        mutate_gene.value = mutate_value
        return mutate_gene

    def mutate_float_gene(self, gene: FloatGene) -> FloatGene:
        mutate_gene = copy.deepcopy(gene)
        bitfield = MathUtil.float_to_bitfield(mutate_gene.value)
        bitfield_size = bitfield.size
        flip_position_1, flip_position_2 = select_mutation_points(start_point=int(bitfield_size * (1 / 10)),
                                                                  stop_point=bitfield_size - 1, amount=2)
        mutate_bitfield = MathUtil.flip_bit(bitfield=bitfield, pos=flip_position_1)
        mutate_bitfield = MathUtil.flip_bit(bitfield=mutate_bitfield, pos=flip_position_2)
        mutate_value = MathUtil.bitfield_to_float(mutate_bitfield)
        mutate_value = crop_to_boundaries(mutate_gene, mutate_value)
        mutate_gene.value = mutate_value
        return mutate_gene


class NonuniformMutation(Mutation):

    def mutate_integer_gene(self, gene: IntegerGene) -> IntegerGene:
        mutate_gene = copy.deepcopy(gene)
        max_val, min_val = max_min_delta(mutate_gene)
        mutate_delta = MathUtil.normal_int_delta(min_val=min_val, max_val=max_val)
        mutate_value = mutate_gene.value + mutate_delta
        mutate_value = crop_to_boundaries(mutate_gene, mutate_value)
        mutate_gene.value = mutate_value
        return mutate_gene

    def mutate_float_gene(self, gene: FloatGene) -> FloatGene:
        mutate_gene = copy.deepcopy(gene)
        max_val, min_val = max_min_delta(mutate_gene)
        mutate_delta = MathUtil.normal_float_delta(min_val=min_val, max_val=max_val)
        mutate_value = mutate_gene.value + mutate_delta
        mutate_value = crop_to_boundaries(mutate_gene, mutate_value)
        mutate_gene.value = mutate_value
        return mutate_gene
