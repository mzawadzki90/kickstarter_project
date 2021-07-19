from genetic_algorithm.crossover import OnePointCrossover
from genetic_algorithm.gene import Gene, FloatGene
from genetic_algorithm.genetic_algorithm import GeneticAlgorithm
from genetic_algorithm.genome import Genome, LabeledSequence
from genetic_algorithm.initialization import RandomInitialization
from genetic_algorithm.mutation import RandomMutation
from genetic_algorithm.parent_selection import TournamentSelection


class GeneticAlgorithmImpl(GeneticAlgorithm):

    def init_population(self, ):
        return RandomInitialization(self.population_size, self.genome).init_population()

    def select_parents(self, fitness):
        return TournamentSelection().select_parents(self.population, fitness)

    def crossover(self, parents):
        return OnePointCrossover().crossover(parents)

    def mutate(self, crossovers):
        return RandomMutation().mutate(crossovers)


labeled_sequence = LabeledSequence()
labeled_sequence.append(FloatGene(label='A', minimum=-10.0, maximum=10))
labeled_sequence.append(FloatGene(label='B', minimum=-10.0, maximum=10))
labeled_sequence.append(FloatGene(label='C', minimum=-10.0, maximum=10))
labeled_sequence.append(FloatGene(label='D', minimum=-10.0, maximum=10))


def rank(params: LabeledSequence[Gene]):
    return 4 * params.get_by_label('A').value - 2 * params.get_by_label('B').value + 3 * params.get_by_label(
        'C').value - params.get_by_label('D').value


genome = Genome(genes=labeled_sequence, rank_funk=rank)
algorithm_impl = GeneticAlgorithmImpl(genome=genome, population_size=5, generation_count=1000,
                                      best_last_generations_size=5)
algorithm_impl.calculate()
