import matplotlib.pyplot as plt
import numpy as np


class RealPredPlotter(object):
    real: np.ndarray
    pred: np.ndarray
    real_dim: int
    pred_dim: int

    def __init__(self, real: np.ndarray, pred: np.ndarray) -> None:
        self.real = real
        self.pred = pred
        self.real_dim = real.shape[0]
        self.pred_dim = pred.shape[0]

    def plot(self):
        plt.plot(range(self.real_dim), self.real, 'ro')
        plt.plot(range(self.pred_dim), self.pred, 'bo')
        plt.title('real/prediction')
        plt.ylabel('popularity')
        plt.xlabel('sample')
        plt.legend(['real', 'prediction'], loc='upper left')
        plt.show()
