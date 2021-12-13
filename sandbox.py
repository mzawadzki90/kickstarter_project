import matplotlib.pyplot as plt
from scipy.stats import truncnorm


def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


X1 = get_truncated_normal(mean=0, sd=1, low=-5, upp=5)
rvs = X1.rvs(size=100000, random_state=True)

fig_1 = plt.figure()
ax_1 = fig_1.add_subplot(1, 1, 1)
ax_1.hist(rvs)
plt.show()

print('4-5', (rvs >= 4.0).sum())
print('3-4', (rvs >= 3.0).sum())
print('2-3', (rvs >= 2.0).sum())
print('1-2', (rvs >= 1.0).sum())
print('0-1', (rvs >= 0.0).sum())
