import copy
from typing import Union, Sequence

from genetic_algorithm.gene import Gene, IntegerGene, FloatGene
from genetic_algorithm.genome import Genome
from utils.math import MathUtil

numeric = Union[int, float]


class Mutation:
    def mutate(self, crossovers: Sequence[Genome]) -> Sequence[Genome]:
        mutate1 = self.get_mutate(crossovers[0])
        mutate2 = self.get_mutate(crossovers[1])
        return [mutate1, mutate2]

    def get_mutate(self, crossover: Genome) -> Genome:
        pass


class RandomMutation(Mutation):

    def get_mutate(self, crossover: Genome) -> Genome:
        mutate = copy.deepcopy(crossover)
        mutation_position_1 = MathUtil.random_int_from_range(0, len(crossover.genes) - 1)
        mutate.genes[mutation_position_1] = self.__get_mutate_gene(crossover.genes[mutation_position_1])
        mutation_position_2 = MathUtil.random_int_from_range(0, len(crossover.genes) - 1)
        mutate.genes[mutation_position_2] = self.__get_mutate_gene(crossover.genes[mutation_position_2])
        return mutate

    def __get_mutate_gene(self, gene: Gene) -> Gene:
        if isinstance(gene, IntegerGene):
            return self.__mutate_integer_gene(gene)
        elif isinstance(gene, FloatGene):
            return self.__mutate_float_gene(gene)

    def __mutate_integer_gene(self, gene: IntegerGene) -> IntegerGene:
        mutate_gene = copy.deepcopy(gene)
        bitfield = MathUtil.integer_to_bitfield(mutate_gene.value)
        flip_position = MathUtil.random_int_from_range(int(bitfield.size * (1 / 10)), bitfield.size - 1)
        mutate_bitfield = MathUtil.flip_bit(bitfield, flip_position)
        flip_position_2 = MathUtil.random_int_from_range(int(bitfield.size * (1 / 10)), bitfield.size - 1)
        mutate_bitfield = MathUtil.flip_bit(mutate_bitfield, flip_position_2)
        mutate_value = MathUtil.bitfield_to_integer(mutate_bitfield)
        mutate_value = self.__crop_to_boundries(mutate_gene, mutate_value)
        mutate_gene.value = mutate_value
        return mutate_gene

    def __mutate_float_gene(self, gene: FloatGene) -> FloatGene:
        mutate_gene = copy.deepcopy(gene)
        bitfield = MathUtil.float_to_bitfield(mutate_gene.value)
        flip_position_1 = MathUtil.random_int_from_range(int(bitfield.size * (1 / 10)), bitfield.size - 1)
        mutate_bitfield = MathUtil.flip_bit(bitfield, flip_position_1)
        flip_position_2 = MathUtil.random_int_from_range(int(bitfield.size * (1 / 10)), bitfield.size - 1)
        mutate_bitfield = MathUtil.flip_bit(mutate_bitfield, flip_position_2)
        mutate_value = MathUtil.bitfield_to_float(mutate_bitfield)
        mutate_value = self.__crop_to_boundries(mutate_gene, mutate_value)
        mutate_gene.value = mutate_value
        return mutate_gene

    def __crop_to_boundries(self, mutate_gene: Gene, mutate_value: numeric) -> numeric:
        maximum = mutate_gene.maximum
        if mutate_value > maximum:
            mutate_value = maximum
        minimum = mutate_gene.minimum
        if mutate_value < minimum:
            mutate_value = minimum
        return mutate_value
