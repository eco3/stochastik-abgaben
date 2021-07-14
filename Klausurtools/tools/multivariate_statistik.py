import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


def lineare_korrelation(a, b):
    print("Legende (3)\n")

    korrelationskoeffizient = np.corrcoef(a, b)[0][1]
    kovarianz = np.cov(a, b)[0][1]

    print(f"(empirischer) Korrelationskoeffizient\t", "np.corrcoef(...)\t", f"r_x,y = {korrelationskoeffizient}")
    print(f"(empirische) Kovarianz\t\t\t", "np.cov(...)\t\t", f"s_x,y = {kovarianz}")


def lineare_regression(a, b):
    print("Legende (4)\n")

    reg = stats.linregress(a, b)

    print("Lineare Regression")
    print(f"f(x) = {reg.slope:.3f} * x + {reg.intercept:.3f}")
    print(f"Bestimmheitsmaß: R² = {reg.rvalue**2}")


def plot_regression(a, b):
    reg = stats.linregress(a, b)

    plt.plot(a, b, 'o', label='original data')
    plt.plot(a, reg.intercept + reg.slope * np.asarray(a), 'r', label='fitted line')
    plt.legend()
    plt.show()
