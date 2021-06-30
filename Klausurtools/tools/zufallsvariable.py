from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def diskrete_zufallsvariable(ps, xs=None):
    if xs is None:
        xs = np.arange(1, len(ps) + 1)

    diskrete_zv = stats.rv_discrete(values=(xs, ps))

    print("ps\t\t", ps)
    print("xs\t\t", xs)
    print()

    print("Erwartungswert\t\t",        "stats.rv_discrete(...).expect()", "\t",      diskrete_zv.expect())
    print("Varianz\t\t\t",             "stats.rv_discrete(...).var()", "\t\t",       diskrete_zv.var())
    print("Standardabweichung\t",      "stats.rv_discrete(...).std()", "\t\t",       diskrete_zv.std())

    return diskrete_zv, xs


def plot_diskrete_zv(ps, xs=None):
    diskrete_zv, xs_tmp = diskrete_zufallsvariable(ps, xs)

    fig, ax = plt.subplots(1, 1)
    ax.plot(xs_tmp, diskrete_zv.pmf(xs_tmp), 'ro', ms=12, mec='r')
    ax.vlines(xs_tmp, 0, diskrete_zv.pmf(xs_tmp), colors='r', lw=4)

    ax.set_title("Verteilung von X | P(X=x)")

    plt.show()

    return diskrete_zv, xs_tmp

