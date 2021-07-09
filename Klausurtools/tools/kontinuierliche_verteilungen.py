from scipy import stats


def _calculate_properties(distribution, code_string):
    print("-----------------------------")
    print("Erwartungswert\t\t",        f"{code_string}.expect()", "\t",      distribution.expect())
    print("Varianz\t\t\t",             f"{code_string}.var()", "\t",       distribution.var())
    print("Standardabweichung\t",      f"{code_string}.std()", "\t",       distribution.std())
    print()


def gleichverteilung(a, b):
    X = stats.uniform(a, b - a)

    print(f"stats.uniform(a={a}, b-a={b-a})", "\t", f"X ~ U({a}, {b})")
    _calculate_properties(X, f"stats.uniform(a={a}, b-a={b-a})")

    return X


def exponentialverteilung(l):
    X = stats.expon(scale=1 / l)

    print(f"stats.expon(scale=1/{l})", "\t", f"X ~ exp({l})")
    _calculate_properties(X, f"stats.expon(scale=1/{l})")

    return X


def normalverteilung(mu, sigma):
    X = stats.norm(mu, sigma)

    print(f"stats.norm(mu={mu}, sigma={sigma})", "\t", f"X ~ N({mu}, {sigma})")
    _calculate_properties(X, f"stats.norm(mu={mu}, sigma={sigma})")

    return X
