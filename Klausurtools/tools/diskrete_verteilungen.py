from scipy import stats

from types import MethodType
from . import diskrete_helper_functions as dhf


def _calculate_properties(distribution, code_string):
    print("-----------------------------")
    print("Erwartungswert\t\t",        f"{code_string}.expect()", "\t",      distribution.expect())
    print("Varianz\t\t\t",             f"{code_string}.var()", "\t",       distribution.var())
    print("Standardabweichung\t",      f"{code_string}.std()", "\t",       distribution.std())
    print()


def _set_helper_methods(discrete_distr):
    discrete_distr.genau = MethodType(dhf.genau, discrete_distr)
    discrete_distr.hoechstens = MethodType(dhf.hoechstens, discrete_distr)
    discrete_distr.mindestens = MethodType(dhf.mindestens, discrete_distr)
    discrete_distr.mehr_als = MethodType(dhf.mehr_als, discrete_distr)
    discrete_distr.weniger_als = MethodType(dhf.weniger_als, discrete_distr)

    return discrete_distr


def bernoulli(p):
    X = _set_helper_methods(stats.bernoulli(p))

    print(f"stats.bernoulli(p={p})", "\t", f"X ~ Ber({p})")
    _calculate_properties(X, f"stats.bernoulli(p={p})")

    return X


def geometrisch(p):
    X = _set_helper_methods(stats.geom(p))

    print(f"stats.geom(p={p})", "\t", f"X ~ geom({p})")
    _calculate_properties(X, f"stats.geom(p={p})")

    return X


def binomial(n, p):
    X = _set_helper_methods(stats.binom(n, p))

    print(f"stats.binom(n={n}, p={p})", "\t", f"X ~ Bin({n}, {p})")
    _calculate_properties(X, f"stats.binom(n={n}, p={p})")

    return X


def poisson(l):
    X = _set_helper_methods(stats.poisson(l))

    print(f"stats.poisson({l})", "\t", f"X ~ Po({l})")
    _calculate_properties(X, f"stats.poisson({l})")

    return X


def hypergeometrisch(N, M, n):
    X = _set_helper_methods(stats.hypergeom(N, M, n))

    print(f"stats.hypergeom(N={N}, M={M}, n={n})", "\t", f"X ~ H({n}, {M}, {N})")
    _calculate_properties(X, f"stats.hypergeom(N={N}, M={M}, n={n})")

    return X
