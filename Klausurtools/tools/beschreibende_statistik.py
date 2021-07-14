import numpy as np
from scipy import stats


def kennwerte(stichprobe):
    print("Legende (1)\n")

    print("Stichprobe\t", stichprobe)
    print()

    print("arithmetische Mittel / Mittelwert\t",        "np.mean(...)",   "\t\t",     np.mean(stichprobe))
    print("Median / Zentralwert\t\t\t",                 "np.median(...)", "\t",       np.median(stichprobe))
    print("Modalwert\t\t\t\t",                          "stats.mode(...)", "\t",      stats.mode(stichprobe))
    print("Quartile\t\t\t\t",                           "np.quantile(...)", "\t",     np.quantile(stichprobe, [0.25, 0.5, 0.75], interpolation="midpoint"))
    print("Varianz / empirische Varianz\t\t",           "np.var(...)", "\t\t",        np.var(stichprobe, ddof=1))
    print("Standardabweichung / empirische Std\t",      "np.std(...)", "\t\t",        np.std(stichprobe, ddof=1))
    print("Spannweite\t\t\t\t",                         "np.max/min(...)", "\t",      np.max(stichprobe) - np.min(stichprobe))
    print("Interquartilabstand\t\t\t",                  "np.quantile(...)", "\t",     np.quantile(stichprobe, 0.75, interpolation="midpoint") - np.quantile(stichprobe, 0.25, interpolation="midpoint"))
    print("empirische Schiefe\t\t\t",                   "stats.skew(...)", "\t",      stats.skew(stichprobe))
    print("empirische Wölbung\t\t\t",                   "stats.kurtosis(...)", "\t",  stats.kurtosis(stichprobe))


def haeufigkeitsverteilung(stichprobe):
    print("Legende (2)\n")

    print("Stichprobe\t", stichprobe)
    print()

    print("Anzahl Messwerte\t\t\t",                     "len(...)", "\t\t\t\t",                         len(stichprobe))
    print("verschiedene auftretende Messwerte\t",       "np.unique(...)", "\t\t\t",                     np.unique(stichprobe))
    print("absolute Häufigkeiten\t\t\t",                "np.unique(..., return_counts=True)", "\t",     np.unique(stichprobe, return_counts=True)[1])
    print("relative Häufigkeiten\t\t\t",                "np.unique(..., return_counts=True)", "\t",     np.unique(stichprobe, return_counts=True)[1] / len(stichprobe))
