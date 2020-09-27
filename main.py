from genetic_algorithm import AbstractGeneticAlgorithm
from tournament_selection import TournamentSelection

aga = AbstractGeneticAlgorithm(5, 10)
population = aga.population
print(population)

fitness = aga.calculate_population_fitness()
print(fitness)

ts = TournamentSelection()
parent1, parent2 = ts.select_parents(population, fitness)
print(parent1)
print(parent2)
