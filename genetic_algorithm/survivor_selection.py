from typing import Sequence

from genetic_algorithm.genome import Genome


class SurvivorSelection:
    def select_survivor(self, mutates: Sequence[Genome]) -> Sequence[Genome]:
        pass


class SelectBest(SurvivorSelection):
    def select_survivor(self, mutates: Sequence[Genome]) -> Sequence[Genome]:
        return [min(mutates, key=lambda g: g.fitness)]


class NoSelection(SurvivorSelection):
    def select_survivor(self, mutates: Sequence[Genome]) -> Sequence[Genome]:
        return mutates
