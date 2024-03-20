import math
import matplotlib.pyplot as plt

def CompositeSimpson(f, a, b, M):
    h = (b - a) / M
    CQ = f(a) + 4*f(a + h/2) + f(b)
    CQ += sum([2*f(a + m*h) + 4*f(a + m*h + h/2) for m in range(1, M)])
    CQ *= h/6

    return CQ

def TestCompositeSimpson():
    for i in range(1, 5):
        CQ = CompositeSimpson(lambda x : math.cos(x), 0, 10, 64 * i)
        E = CQ - math.sin(10)
        print(abs(E))

def TrapezoidQuadrature(f, a, b):
    return (b - a) * ((f(a) + f(b)) / 2)

def AdaptiveTrapeziod(f, a, b, tol, a0, b0, s):
    c = (a + b) / 2

    Q = TrapezoidQuadrature(f, a, b)
    Qstar = TrapezoidQuadrature(f, a, c)
    Qstarstar = TrapezoidQuadrature(f, c, b)

    s.add(a)
    s.add(b)

    if abs(Q - Qstar - Qstarstar) < 3*tol*((b - a) / (b0 - a0)):
        return Qstar + Qstarstar
    else:
        return AdaptiveTrapeziod(f, a, c, tol, a0, b0, s) + AdaptiveTrapeziod(f, c, b, tol, a0, b0, s)

def SimpsonQuadrature(f, a, b):
    return ((b - a) / 6) * (f(a) + 4*f((a + b) / 2) + f(b))

def AdaptiveSimpson(f, a, b, tol, a0, b0, s):
    c = (a + b) / 2

    Q = SimpsonQuadrature(f, a, b)
    Qstar = SimpsonQuadrature(f, a, c)
    Qstarstar = SimpsonQuadrature(f, c, b)

    s.add(a)
    s.add(b)

    if abs(Q - Qstar - Qstarstar) < 15*tol*((b - a) / (b0 - a0)):
        return Qstar + Qstarstar
    else:
        return AdaptiveSimpson(f, a, c, tol, a0, b0, s) + AdaptiveSimpson(f, c, b, tol, a0, b0, s)

def TestAdaptiveTrapezoid(f, a, b):
    xs = set()
    print(AdaptiveTrapeziod(f, a, b, 0.5/(10**8), a, b, xs))

    ps = [(x, f(x)) for x in xs]
    plt.scatter([p[0] for p in ps], [p[1] for p in ps])
    plt.show()

def TestAdaptiveSimpson():
    f = lambda x : math.exp((-x**2) / 2)
    xs = set()

    sd = 3
    res = (1/math.sqrt(2 * math.pi)) * AdaptiveSimpson(f, -sd, sd, 0.5/(10**8), -sd, sd, xs)
    print(res)

    ps = [(x, f(x)) for x in xs]
    plt.scatter([p[0] for p in ps], [p[1] for p in ps])
    plt.show()


if __name__ == "__main__":
    # TestCompositeSimpson()
    # TestAdaptiveTrapezoid(lambda x : math.exp(x**2.0), 0, 1)
    # TestAdaptiveTrapezoid(lambda x : math.sin(x**2), 0, math.sqrt(math.pi))
    # TestAdaptiveTrapezoid(lambda x : x**x, 0, 1)
    TestAdaptiveSimpson()
