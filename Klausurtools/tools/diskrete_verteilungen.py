from scipy import stats


def _calculate_properties(distribution, code_string):
    print("-----------------------------")
    print("Erwartungswert\t\t",        f"{code_string}.expect()", "\t",      distribution.expect())
    print("Varianz\t\t\t",             f"{code_string}.var()", "\t",       distribution.var())
    print("Standardabweichung\t",      f"{code_string}.std()", "\t",       distribution.std())
    print()


def bernoulli(p):
    X = stats.bernoulli(p)

    print(f"stats.bernoulli(p={p})", "\t", f"X ~ Ber({p})")
    _calculate_properties(X, f"stats.bernoulli(p={p})")

    return X


def geometrisch(p):
    X = stats.geom(p)

    print(f"stats.geom(p={p})", "\t", f"X ~ geom({p})")
    _calculate_properties(X, f"stats.geom(p={p})")

    return X


def binomial(n, p):
    X = stats.binom(n, p)

    print(f"stats.binom(n={n}, p={p})", "\t", f"X ~ Bin({n}, {p})")
    _calculate_properties(X, f"stats.binom(n={n}, p={p})")

    return X


def poisson(l):
    X = stats.poisson(l)

    print(f"stats.poisson({l})", "\t", f"X ~ Po({l})")
    _calculate_properties(X, f"stats.poisson({l})")

    return X


def hypergeometrisch(N, M, n):
    X = stats.hypergeom(N, M, n)

    print(f"stats.hypergeom(N={N}, M={M}, n={n})", "\t", f"X ~ H({n}, {M}, {N})")
    _calculate_properties(X, f"stats.hypergeom(N={N}, M={M}, n={n})")

    return X
