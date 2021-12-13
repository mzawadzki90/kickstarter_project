from typing import Sequence, MutableSequence

import numpy as np

from genetic_algorithm.crossover import OnePointCrossover
from genetic_algorithm.gene import Gene, FloatGene
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm
from genetic_algorithm.genome import Genome, LabeledSequence
from genetic_algorithm.initialization import RandomInitialization
from genetic_algorithm.mutation import NonuniformMutation
from genetic_algorithm.parent_selection import TournamentSelection


class GeneticAlgorithmImpl(GeneticAlgorithm):

    def init_population(self) -> MutableSequence[Genome]:
        return RandomInitialization(self.population_size, self.genome).init_population()

    def select_parents(self, fitness: np.ndarray, worst_from_previous_generations: float) -> Sequence[Genome]:
        return TournamentSelection().select_parents(self.population, fitness, self.worst_from_previous_generations)

    def crossover(self, parents: Sequence[Genome]) -> Sequence[Genome]:
        return OnePointCrossover().crossover(parents)

    def mutate(self, crossovers: Sequence[Genome]) -> Sequence[Genome]:
        return NonuniformMutation().mutate(crossovers)


labeled_sequence = LabeledSequence()
labeled_sequence.append(FloatGene(label='A', minimum=-10.0, maximum=10.0))
labeled_sequence.append(FloatGene(label='B', minimum=-10.0, maximum=10.0))
labeled_sequence.append(FloatGene(label='C', minimum=-10.0, maximum=10.0))
labeled_sequence.append(FloatGene(label='D', minimum=-10.0, maximum=10.0))


def rank(params: LabeledSequence[Gene]):
    return abs(params.get_by_label('A').value * params.get_by_label('B').value * params.get_by_label(
        'C').value * params.get_by_label('D').value)


genome = Genome(genes=labeled_sequence, rank_funk=rank)
algorithm_impl = GeneticAlgorithmImpl(genome=genome, population_size=5, generation_count=1000,
                                      best_last_generations_size=5)
algorithm_impl.calculate()
