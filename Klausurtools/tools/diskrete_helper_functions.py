
def hoechstens(self, wert):
    val = self.cdf(wert)

    print(self.__class__.__name__)

    print(f"P(X≤{wert}) =", val, f"  |  .cdf({wert})")


def mindestens(ZV, wert):
    val = 1 - ZV.cdf(wert - 1)

    print(f"P(X≥{wert}) = 1-P(X≤{wert-1}) =", val, f"  |  .cdf({wert-1})")


def mehr_als(ZV, wert):
    val = 1 - ZV.cdf(wert)

    print(f"P(X>{wert}) = 1-P(X≤{wert}) =", val, f"  |  .cdf({wert})")


def weniger_als(ZV, wert):
    val = ZV.cdf(wert - 1)

    print(f"P(X<{wert}) = P(X≤{wert-1}) =", val, f"  |  .cdf({wert-1})")


def genau(ZV, wert):
    val = ZV.cdf(wert)

    print(f"P(X={wert}) =", val, f"  |  .cdf({wert})")
