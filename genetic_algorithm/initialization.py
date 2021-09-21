import random
from typing import Sequence

from genetic_algorithm.gene import Gene
from genetic_algorithm.genome import Genome, LabeledSequence


class PopulationInitializer:
    population_size: int
    initial_genome: Genome

    def __init__(self, population_size: int, initial_genome: Genome):
        self.population_size = population_size
        self.initial_genome = initial_genome

    def init_population(self) -> Sequence[Genome]:
        pass


class RandomInitialization(PopulationInitializer):

    def init_population(self) -> Sequence[Genome]:
        init_genes = self.initial_genome.genes
        rank = self.initial_genome.rank_func
        population = []
        for x in range(0, self.population_size):
            genes = LabeledSequence()
            for gene in init_genes:
                label = gene.label
                minimum = gene.minimum
                maximum = gene.maximum
                if gene.get_type() == int.__class__:
                    genes.append(
                        Gene(label=label, minimum=minimum, maximum=maximum, value=random.randint(minimum, maximum)))
                elif gene.get_type() == float.__class__:
                    genes.append(
                        Gene(label=label, minimum=minimum, maximum=maximum, value=random.uniform(minimum, maximum)))
            population.append(Genome(genes, rank))
        return population
