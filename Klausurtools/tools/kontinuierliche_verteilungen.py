from scipy import stats

from types import MethodType
from . import kontinuierliche_helper_functions as khf


def _calculate_properties(distribution, code_string):
    print("-----------------------------")
    print("Erwartungswert\t\t",        f"{code_string}.expect()", "\t",      distribution.expect())
    print("Varianz\t\t\t",             f"{code_string}.var()", "\t",       distribution.var())
    print("Standardabweichung\t",      f"{code_string}.std()", "\t",       distribution.std())
    print()


def _set_helper_methods(continous_distr):
    continous_distr.genau = MethodType(khf.genau, continous_distr)
    continous_distr.hoechstens = MethodType(khf.hoechstens, continous_distr)
    continous_distr.mindestens = MethodType(khf.mindestens, continous_distr)
    continous_distr.mehr_als = MethodType(khf.mehr_als, continous_distr)
    continous_distr.weniger_als = MethodType(khf.weniger_als, continous_distr)
    continous_distr.zwischen = MethodType(khf.zwischen, continous_distr)

    return continous_distr


def gleichverteilung(a, b):
    print("Legende (18)\n")

    X = _set_helper_methods(stats.uniform(a, b - a))

    print(f"stats.uniform(a={a}, b-a={b-a})", "\t", f"X ~ U({a}, {b})")
    _calculate_properties(X, f"stats.uniform(a={a}, b-a={b-a})")

    return X


def exponentialverteilung(l):
    print("Legende (19)\n")

    X = _set_helper_methods(stats.expon(scale=1 / l))

    print(f"stats.expon(scale=1/{l})", "\t", f"X ~ exp({l})")
    _calculate_properties(X, f"stats.expon(scale=1/{l})")

    return X


def normalverteilung(mu, sigma):
    print("Legende (20)\n")

    X = _set_helper_methods(stats.norm(mu, sigma))

    print(f"stats.norm(mu={mu}, sigma={sigma})", "\t", f"X ~ N({mu}, {sigma})")
    _calculate_properties(X, f"stats.norm(mu={mu}, sigma={sigma})")

    print("68-95-99.7-Regel / 3-sigma-Grenzen")
    print(f"   68.3%: [mu -   sigma, mu +   sigma] = [{mu - sigma}, {mu + sigma}]")
    print(f"   95.5%: [mu - 2*sigma, mu + 2*sigma] = [{mu - 2*sigma}, {mu + 2*sigma}]")
    print(f"   99.7%: [mu - 3*sigma, mu + 3*sigma] = [{mu - 3*sigma}, {mu + 3*sigma}]")
    print()

    return X
