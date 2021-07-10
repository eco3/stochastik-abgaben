def hoechstens(self, wert):
    val = self.cdf(wert)
    print(f"P(X≤{wert}) =", val, f"  |  .cdf({wert})")
    return val


def mindestens(self, wert):
    val = 1 - self.cdf(wert - 1)
    print(f"P(X≥{wert}) = 1-P(X≤{wert-1}) =", val, f"  |  .cdf({wert-1})")
    return val


def mehr_als(self, wert):
    val = 1 - self.cdf(wert)
    print(f"P(X>{wert}) = 1-P(X≤{wert}) =", val, f"  |  .cdf({wert})")
    return val


def weniger_als(self, wert):
    val = self.cdf(wert - 1)
    print(f"P(X<{wert}) = P(X≤{wert-1}) =", val, f"  |  .cdf({wert-1})")
    return val


def genau(self, wert):
    val = self.pmf(wert)
    print(f"P(X={wert}) =", val, f"  |  .cdf({wert})")
    return val
