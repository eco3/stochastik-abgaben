def hoechstens(self, wert):
    val = self.cdf(wert)
    print(f"P(X≤{wert}) = F({wert}) =", val, f"  |  .cdf({wert})")
    return val


def mindestens(self, wert):
    val = 1 - self.cdf(wert)
    print(f"P(X≥{wert}) = 1-P(X<{wert}) = 1-F({wert}) =", val, f"  |  .cdf({wert})")
    return val


def mehr_als(self, wert):
    val = 1 - self.cdf(wert)
    print(f"P(X>{wert}) = 1-P(X≤{wert}) = 1-F({wert}) =", val, f"  |  .cdf({wert})")
    return val


def weniger_als(self, wert):
    val = self.cdf(wert)
    print(f"P(X<{wert}) = P(X≤{wert}) = F({wert}) =", val, f"  |  .cdf({wert})")
    return val


def genau(self, wert):
    val = 0
    print(f"P(X={wert}) =", val, f"  |  (wie bei jeder stetigen Zufallsvariable)")
    return val


def zwischen(self, a, b):
    val = self.cdf(b) - self.cdf(a)
    print(f"P({a}≤X≤{b}) = F({b})-F({a}) =", val, f"  |  .cdf({b}) - .cdf({a})")
    return val
