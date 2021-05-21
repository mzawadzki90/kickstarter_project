import numpy as np

from utils.math import MathUtil


class Crossover:
    def crossover(self, parents: np.ndarray) -> np.ndarray:
        pass


def select_crossover_point(size: int) -> int:
    if size % 2 == 0:
        return int(size / 2)
    else:
        return int(size / 2 + 1)


class OnePointCrossover(Crossover):
    def crossover(self, parents: np.ndarray) -> np.ndarray:
        parent1 = parents[0]
        parent2 = parents[1]
        crossover_point = select_crossover_point(parent1.size)
        crossover1 = np.concatenate((parent1[0:crossover_point], parent2[crossover_point:]))
        crossover2 = np.concatenate((parent2[0:crossover_point], parent1[crossover_point:]))
        return np.array([crossover1, crossover2])


class OnePointBinaryCrossover(Crossover):
    def crossover(self, parents: np.ndarray) -> np.ndarray:
        parent1 = parents[0][0]
        parent2 = parents[1][0]
        parent1_bitfield = MathUtil.float_to_bitfield(parent1)
        parent2_bitfield = MathUtil.float_to_bitfield(parent2)
        if len(parent1_bitfield) != len(parent2_bitfield):
            parent1_bitfield, parent2_bitfield = MathUtil.set_equal_length(parent1_bitfield, parent2_bitfield)
        crossover_point = select_crossover_point(parent1_bitfield.size)
        crossover1_bitfield = np.concatenate((parent1_bitfield[0:crossover_point], parent2_bitfield[crossover_point:]))
        crossover2_bitfield = np.concatenate((parent1_bitfield[0:crossover_point], parent2_bitfield[crossover_point:]))
        crossover1 = MathUtil.bitfield_to_float(crossover1_bitfield)
        crossover2 = MathUtil.bitfield_to_float(crossover2_bitfield)
        return np.array([np.array([crossover1]), np.array([crossover2])])
