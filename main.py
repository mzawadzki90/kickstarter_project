from genetic_algorithm import AbstractGeneticAlgorithm

population = AbstractGeneticAlgorithm.init_population(5, 10)
print(population)

fitness = AbstractGeneticAlgorithm.calculate_population_fitness(population)
print(fitness)
