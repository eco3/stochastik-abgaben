from scipy import special


def permutation(n):
    value = special.factorial(n, exact=True)

    print("Permutation\t\t\t", "special.factorial(n, exact=True)", "\t", value)

    return value


def variation(n, k, wiederholung):
    if wiederholung:
        value = pow(n, k)
        print("Variation mit Wiederholung\t", "pow(n, k)", "\t", value)
    else:
        value = special.perm(n, k, exact=True)
        print("Variation ohne Wiederholung\t", "special.perm(n, k, exact=True)", "\t", value)

    return value


def kombination(n, k, wiederholung):
    value = special.comb(n, k, repetition=wiederholung, exact=True)

    if wiederholung:
        print("Kombination mit Wiederholung\t", "special.comb(n, k, repetition=True, exact=True)", "\t", value)
    else:
        print("Kombination ohne Wiederholung\t", "special.comb(n, k, repetition=False, exact=True)", "\t", value)

    return value