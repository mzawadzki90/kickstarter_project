from genetic_algorithm import AbstractGeneticAlgorithm
from one_point_crossover import OnePointCrossover
from tournament_selection import TournamentSelection

aga = AbstractGeneticAlgorithm(5, 10)
population = aga.population
print(population)

fitness = aga.calculate_population_fitness()
print(fitness)

ts = TournamentSelection()
parents = ts.select_parents(population, fitness)
print(parents[0])
print(parents[1])

opc = OnePointCrossover()
crossovers = opc.crossover(parents)
print(crossovers[0])
print(crossovers[1])
