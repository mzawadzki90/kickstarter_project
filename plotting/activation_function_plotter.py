import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes


def relu(x: np.ndarray) -> np.ndarray:
    return x * (x > 0)


def elu(x: np.ndarray, alfa: int = 1) -> np.ndarray:
    return np.where(x < 0, alfa * (np.exp(x) - 1), x)


def set_ax(ax: Axes) -> None:
    left = ax.spines['left']
    left.set_position('center')
    left.set_linewidth(1.1)
    bottom = ax.spines['bottom']
    bottom.set_position(('data', 0.0))
    bottom.set_linewidth(1.1)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')


dirname = os.getcwd()

# plot ReLU function

x = np.linspace(-5, 5, 100)
y = relu(x)

fig_1 = plt.figure()
ax_1 = fig_1.add_subplot(1, 1, 1)
set_ax(ax_1)

plt.title('Funkcja aktywacji ReLU')
plt.grid(True)
plt.plot(x, y, color='blue', linewidth=2.0)

plt.savefig(os.path.join(dirname, 'out\\relu.eps'))

# plot ELU function

x = np.linspace(-5, 5, 100)
y = elu(x)

fig_2 = plt.figure()
ax_2 = fig_2.add_subplot(1, 1, 1)
set_ax(ax_2)

title = r'Funkcja aktywacji ELU ($\alpha$ = 1)'
plt.title(title)
plt.grid(True)
plt.axhline(y=-1, color="black", linestyle="--", linewidth=1.5)
plt.plot(x, y, color='blue', linewidth=2.0)

plt.savefig(os.path.join(dirname, 'out\\elu.eps'))
