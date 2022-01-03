from typing import Sequence, MutableSequence

import numpy as np

from genetic_algorithm.crossover import TwoPointsCrossover
from genetic_algorithm.gene import Gene, FloatGene, IntegerGene
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm
from genetic_algorithm.genome import Genome, LabeledSequence
from genetic_algorithm.initialization import RandomInitialization
from genetic_algorithm.mutation import NonuniformMutation
from genetic_algorithm.parent_selection import TournamentSelection
from genetic_algorithm.survivor_selection import NoSelection


class GeneticAlgorithmImpl(GeneticAlgorithm):

    def init_population(self) -> MutableSequence[Genome]:
        return RandomInitialization(self.population_size, self.genome).init_population()

    def select_parents(self, fitness: np.ndarray, worst_from_previous_generations: float) -> Sequence[Genome]:
        return TournamentSelection().select_parents(self.population, fitness, worst_from_previous_generations)

    def crossover(self, parents: Sequence[Genome]) -> Sequence[Genome]:
        return TwoPointsCrossover().crossover(parents)

    def mutate(self, crossovers: Sequence[Genome]) -> Sequence[Genome]:
        return NonuniformMutation().mutate(crossovers)

    def select_survivor(self, mutates: Sequence[Genome]) -> Sequence[Genome]:
        return NoSelection().select_survivor(mutates)


labeled_sequence = LabeledSequence()
labeled_sequence.append(FloatGene(label='A', minimum=0.1, maximum=50.0))
labeled_sequence.append(IntegerGene(label='B', minimum=0, maximum=50))
labeled_sequence.append(FloatGene(label='C', minimum=0.1, maximum=50.0))
labeled_sequence.append(IntegerGene(label='D', minimum=0, maximum=50))
labeled_sequence.append(IntegerGene(label='E', minimum=1, maximum=50))
labeled_sequence.append(IntegerGene(label='F', minimum=2, maximum=50))


def rank(params: LabeledSequence[Gene]):
    return abs(params.get_by_label('A').value + params.get_by_label('B').value + params.get_by_label(
        'C').value + params.get_by_label('D').value + params.get_by_label('E').value + params.get_by_label('F').value)


genome = Genome(genes=labeled_sequence, rank_funk=rank)
algorithm_impl = GeneticAlgorithmImpl(genome=genome, population_size=20, generation_count=1000,
                                      best_last_generations_size=5)
algorithm_impl.calculate()
