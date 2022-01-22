import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D


class RealMultiPredPlotter(object):
    real: np.ndarray
    pred_dict: dict
    real_dim: int

    def __init__(self, real: np.ndarray, pred_dict: dict) -> None:
        self.real = real
        self.pred_dict = pred_dict
        self.real_dim = real.shape[0]

    def plot(self):
        fig = plt.figure(figsize=(self.real.shape[0], 10), dpi=80)
        ax = fig.add_subplot(111)

        ax.add_line(Line2D(xdata=range(self.real.shape[0]), ydata=self.real, color='r', marker='x', linestyle=''))

        for label, values in self.pred_dict.items():
            ax.add_line(
                Line2D(xdata=range(values.shape[0]), ydata=values, color=self.choose_rand_color(), marker='x',
                       linestyle=''))

        plt.title('Porównanie wartości rzeczywistych i wybranych predykcji')
        plt.ylabel('Popularność (0-100)')
        plt.xlabel('Przykład')

        legend = ['wartość rzeczywista'] + list(self.pred_dict.keys())
        plt.legend(legend, loc='upper left')

        ax.set_xlim(-1, self.real.shape[0])
        ax.set_ylim(-10, 100)

        plt.tight_layout()
        plt.savefig('plots\\compr_samples_real_predictions.eps')
        plt.show()

    def choose_rand_color(self) -> tuple:
        r = np.random.rand()
        g = np.random.rand()
        b = np.random.rand()
        return r, g, b
