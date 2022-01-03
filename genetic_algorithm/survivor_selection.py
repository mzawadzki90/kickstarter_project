from typing import Sequence

from genetic_algorithm.genome import Genome


class SurvivorSelection:
    def select_survivor(self, mutates: Sequence[Genome]) -> Sequence[Genome]:
        pass


class SelectBest(SurvivorSelection):
    def select_survivor(self, mutates: Sequence[Genome]) -> Sequence[Genome]:
        mutate1 = mutates[0]
        mutate2 = mutates[1]
        if mutate1.fitness <= mutate2.fitness:
            return [mutate1]
        else:
            return [mutate2]


class NoSelection(SurvivorSelection):
    def select_survivor(self, mutates: Sequence[Genome]) -> Sequence[Genome]:
        return mutates
