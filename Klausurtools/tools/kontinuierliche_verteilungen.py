from scipy import stats


def gleichverteilung(a, b):
    print(f"stats.uniform(a={a}, b-a={b-a})")

    return stats.uniform(a, b - a)


def exponentialverteilung(l):
    print(f"stats.expon(scale=1/{l})")

    return stats.expon(scale=1/l)


def normalverteilung(mu, sigma):
    print(f"stats.norm(mu={mu}, sigma={sigma})")

    return stats.norm(mu, sigma)
