import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class HistogramPlotter:
    x: pd.Series
    output_path: str

    def __init__(self, x: pd.Series, output_path: str) -> None:
        self.x = x
        self.output_path = output_path

    def hist(self, figsize: (float, float) = (12, 4), title: str = '', xlabel: str = '', ylabel: str = '',
             xscale: str = 'linear', xmin: float = 0.000001, xmax: float = 1.0, grid: bool = True, color: str = 'blue',
             bins: int = 100,
             alpha: float = 0.7) -> None:
        fig = plt.figure(figsize=figsize, dpi=200)
        fig.add_subplot(1, 1, 1, )
        plt.title(title, fontsize=12)
        plt.xlabel(xlabel, fontsize=11)
        plt.xscale(xscale)
        plt.ylabel(ylabel, fontsize=11)
        plt.grid(grid)

        if xscale == 'log':
            plt.hist(x=self.x, color=color, bins=np.logspace(np.log10(xmin), np.log10(xmax), bins), alpha=alpha)
        else:
            plt.hist(x=self.x, color=color, bins=bins, alpha=alpha)

        cwd = os.getcwd()
        plt.savefig(os.path.join(cwd, self.output_path))
        plt.show()
