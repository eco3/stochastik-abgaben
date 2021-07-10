def hoechstens(self, wert):
    val = self.cdf(wert)
    print(f"P(X≤{wert}) =", val, f"  |  .cdf({wert})")


def mindestens(self, wert):
    val = 1 - self.cdf(wert - 1)
    print(f"P(X≥{wert}) = 1-P(X≤{wert-1}) =", val, f"  |  .cdf({wert-1})")


def mehr_als(self, wert):
    val = 1 - self.cdf(wert)
    print(f"P(X>{wert}) = 1-P(X≤{wert}) =", val, f"  |  .cdf({wert})")


def weniger_als(self, wert):
    val = self.cdf(wert - 1)
    print(f"P(X<{wert}) = P(X≤{wert-1}) =", val, f"  |  .cdf({wert-1})")


def genau(self, wert):
    val = self.cdf(wert)
    print(f"P(X={wert}) =", val, f"  |  .cdf({wert})")
