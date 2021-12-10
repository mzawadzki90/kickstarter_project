from typing import MutableSequence

from genetic_algorithm.gene import IntegerGene, FloatGene
from genetic_algorithm.genome import Genome, LabeledSequence
from utils.math import MathUtil


class PopulationInitializer:
    population_size: int
    initial_genome: Genome

    def __init__(self, population_size: int, initial_genome: Genome):
        self.population_size = population_size
        self.initial_genome = initial_genome

    def init_population(self) -> MutableSequence[Genome]:
        pass


class RandomInitialization(PopulationInitializer):

    def init_population(self) -> MutableSequence[Genome]:
        init_genes = self.initial_genome.genes
        rank = self.initial_genome.rank_func
        population = []
        for x in range(0, self.population_size):
            genes = LabeledSequence()
            for gene in init_genes:
                label = gene.label
                minimum = gene.minimum
                maximum = gene.maximum
                if isinstance(gene, IntegerGene):
                    genes.append(
                        IntegerGene(label=label, minimum=minimum, maximum=maximum,
                                    value=MathUtil.random_int_from_range(minimum, maximum)))
                elif isinstance(gene, FloatGene):
                    genes.append(
                        FloatGene(label=label, minimum=minimum, maximum=maximum,
                                  value=MathUtil.random_float_from_range(minimum, maximum)))
            population.append(Genome(genes, rank))
        return population
