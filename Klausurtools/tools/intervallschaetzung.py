import numpy as np
from scipy import stats


def konfidenzintervall_normalverteilung(alpha, sigma=None, data=None, x_mean=None, s=None, n=None):
    print("Legende (11)\n")

    if data:
        _x_mean = np.mean(data)
        _s = np.std(data, ddof=1)
        _n = len(data)
    else:
        _x_mean = x_mean
        _s = s
        _n = n

    if sigma:
        quantile = abs(stats.norm(0, 1).ppf((1 - alpha) / 2.0))
        ci_factor = sigma / np.sqrt(_n)

        msg = "Konfidenzintervall für Erwartungswert (mu) einer normalvert. ZV X mit unbek. Std. (sigma)"
    elif _s:
        quantile = abs(stats.t(_n - 1).ppf((1 - alpha) / 2.0))
        ci_factor = _s / np.sqrt(_n)

        msg = "Konfidenzintervall für Erwartungswert (mu) einer normalvert. ZV X mit unbek. Std. (sigma)"
    else:
        raise Exception("Sigma oder Std fehlt.")

    confidence_interval = [_x_mean - quantile * ci_factor,
                           _x_mean + quantile * ci_factor]

    print(msg, confidence_interval)

    return confidence_interval


def konfidenzintervall_beliebige_verteilung(alpha, sigma=None, data=None, x_mean=None, s=None, n=None):
    print("Legende (12)\n")

    if data:
        _x_mean = np.mean(data)
        _s = np.std(data, ddof=1)
        _n = len(data)
    else:
        _x_mean = x_mean
        _s = s
        _n = n

    quantile = abs(stats.norm(0, 1).ppf((1 - alpha) / 2.0))

    if sigma:
        ci_factor = sigma / np.sqrt(_n)
    elif _s:
        ci_factor = _s / np.sqrt(_n)
    else:
        raise Exception("Sigma oder Std fehlt.")

    confidence_interval = [_x_mean - quantile * ci_factor,
                           _x_mean + quantile * ci_factor]

    print("Konfidenzintervall für Erwartungswert (mu) einer bel. vert. ZV X, mit n >= 30", confidence_interval)

    return confidence_interval
