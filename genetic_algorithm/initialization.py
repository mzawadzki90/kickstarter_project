import random
from collections.abc import Iterable

from genetic_algorithm.gene import Gene
from genetic_algorithm.genome import Genome


class PopulationInitializer:
    population_size: int
    initial_genome: Genome

    def __init__(self, population_size: int, initial_genome: Genome):
        self.population_size = population_size
        self.initial_genome = initial_genome

    def init_population(self) -> Iterable[Genome]:
        pass


class RandomInitialization(PopulationInitializer):

    def init_population(self) -> Iterable[Genome]:
        init_genes = self.initial_genome.genes
        rank = self.initial_genome.rank
        population = []
        for x in range(0, self.population_size):
            genes = []
            for gene in init_genes:
                minimum = gene.minimum
                maximum = gene.maximum
                if gene.get_type() == int.__class__:
                    genes.append(Gene(random.randint(minimum, maximum), minimum, maximum))
                elif gene.get_type() == float.__class__:
                    genes.append(Gene(random.uniform(minimum, maximum), minimum, maximum))
            population.append(Genome(genes, rank))
        return population
