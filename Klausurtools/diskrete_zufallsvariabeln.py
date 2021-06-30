from tools.zufallsvariable import *


p = [1/6, (5/6) * 1/6, (5/6)**2 * 1/6, (5/6)**3 * 1/6, (5/6)**4]
zv, xs = diskrete_zufallsvariable(p)


# P(X >= 3)
np.sum(zv.pmf([3, 4, 5]))

# P(X = 2)
np.sum(zv.pmf(2))

# P(X <= 5)
np.sum(zv.pmf([1, 2, 3, 4, 5]))
