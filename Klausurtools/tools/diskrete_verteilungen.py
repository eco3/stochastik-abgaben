from scipy import stats


def bernoulli(p):
    print(f"stats.bernoulli(p={p})")

    return stats.bernoulli(p)


def geometrisch(p):
    print(f"stats.geom(p={p})")

    return stats.geom(p)


def binomial(n, p):
    print(f"stats.binom(n={n}, p={p})")

    return stats.binom(n, p)


def poisson(l):
    print(f"stats.poisson(k={l})")

    return stats.poisson(k=l)


def hyper_geometrisch(N, M, n):
    print(f"stats.hypergeom(N={N}, M={M}, n={n})")

    return stats.hypergeom(N, M, n)