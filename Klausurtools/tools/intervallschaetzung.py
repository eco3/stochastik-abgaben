import numpy as np
from scipy import stats


def konfidenzintervall_normalverteilung(data, alpha, sigma=None):
    x_mean = np.mean(data)

    if sigma:
        quantile = stats.norm(0, 1).ppf(1 - alpha/2.0)

        ci_factor = sigma / np.sqrt(len(data))

        msg = "Konfidenzintervall für Erwartungswert (mu) einer normalvert. ZV X mit unbek. Std. (sigma)"
    else:
        quantile = stats.t(len(data) - 1).ppf(1 - alpha/2.0)

        ci_factor = np.std(data, ddof=1) / np.sqrt(len(data))

        msg = "Konfidenzintervall für Erwartungswert (mu) einer normalvert. ZV X mit unbek. Std. (sigma)"

    confidence_interval = [x_mean - quantile * ci_factor,
                           x_mean + quantile * ci_factor]

    print(msg, confidence_interval)

    return confidence_interval


def konfidenzintervall_beliebige_verteilung(data, alpha, sigma=None):
    x_mean = np.mean(data)
    quantile = stats.norm(0, 1).ppf(1 - alpha / 2.0)

    if sigma:
        ci_factor = sigma / np.sqrt(len(data))
    else:
        ci_factor = np.std(data, ddof=1) / np.sqrt(len(data))

    confidence_interval = [x_mean - quantile * ci_factor,
                           x_mean + quantile * ci_factor]

    print("Konfidenzintervall für Erwartungswert (mu) einer bel. vert. ZV X, mit n >= 30", confidence_interval)

    return confidence_interval
