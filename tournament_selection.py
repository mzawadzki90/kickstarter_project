import numpy as np


class TournamentSelection:

    def select_parents(self, population, fitness):
        population_copy = np.copy(population)
        fitness_copy = np.copy(fitness)
        parent1, index1 = self.select_parent(population_copy, fitness_copy)
        population_copy = np.delete(population_copy, index1, axis=0)
        fitness_copy = np.delete(fitness_copy, index1)
        parent2, index2 = self.select_parent(population_copy, fitness_copy)
        return np.array([parent1, parent2])

    def select_parent(self, population, fitness):
        population_rows = population.shape[0]
        candidates = np.random.choice(a=population_rows, size=self.get_candidates_size(population_rows),
                                      p=self.get_probability_arr(fitness))
        candidates_fitness = np.take(fitness, candidates)
        min_candidate_index = np.where(fitness == np.min(candidates_fitness))
        return population[min_candidate_index][0], min_candidate_index[0][0]

    @staticmethod
    def get_probability_arr(fitness):
        fitness_rows = fitness.shape[0]
        if fitness_rows == 1:
            return np.array([1])

        if fitness.std() < 0.001:
            return np.ones(fitness_rows) / fitness_rows

        max_fitness = np.max(fitness)
        fitness_sum = np.sum(fitness)
        reshaped = (max_fitness - fitness) / ((fitness_rows * max_fitness) - fitness_sum)

        return reshaped.tolist()

    @staticmethod
    def get_candidates_size(population_rows):
        return max(2, int(population_rows * 0.3))
