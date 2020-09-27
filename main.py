from genetic_algorithm import AbstractGeneticAlgorithm

aga = AbstractGeneticAlgorithm(5, 10)
print(aga.population)

fitness = aga.calculate_population_fitness()
print(fitness)
