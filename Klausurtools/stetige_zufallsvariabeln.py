import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


class stetige_zv(stats.rv_continuous):
    def _pdf(self, x):
        return np.where((1. <= x) & (x <= 6), (3./215.) * x**2, 0.)


zv = stetige_zv()
x = np.linspace(0, 7, 1000)


# f(x) - PDF / Verteilungsdichte
fig, ax = plt.subplots(1, 1)
ax.plot(x, zv.pdf(x), 'b-')
ax.set_title("f(x) - PDF / Verteilungsdichte")
plt.plot()

# F(x) - CDF / Verteilungsfunktion
fig, ax = plt.subplots(1, 1)
ax.plot(x, zv.cdf(x), 'r-')
ax.set_title("F(x) - CDF / Verteilungsfunktion")
plt.plot()


a = 2
b = 5

# P(X <= b) = F(b)
zv.cdf(b)

# P(a < X <= b) = F(b) - F(a)
zv.cdf(b) - zv.cdf(a)

# P(X > a) = 1 - F(a)
1 - zv.cdf(a)


zv.expect()
zv.median()
zv.mean()
zv.var()
zv.std()
