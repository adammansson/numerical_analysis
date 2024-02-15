import numpy as np
import matplotlib.pyplot as plt

def LagrangePolynomial(i, xs):
    N = len(xs)
    res = np.polynomial.Polynomial([1])
    for k in range(N):
        if k != i:
            res *= (np.polynomial.Polynomial([0, 1]) - xs[k]) / (xs[i] - xs[k])

    return res

def LagrangeInterpolation(xs, f):
    N = len(xs)
    res = np.polynomial.Polynomial([0])
    for i in range(N):
        res += f(xs[i]) * LagrangePolynomial(i, xs)

    return res

def exercise_1():
    N = 20
    xs = [-1 + 2*i/N for i in range(N + 1)]
    f = lambda x : np.exp(-x**2)
    ys = [LagrangeInterpolation(xs, f)(x) for x in xs]
    es = [abs(f(x) - LagrangeInterpolation(xs, f)(x)) for x in xs]

    plt.plot(xs, es)
    plt.show()

if __name__ == "__main__":
    exercise_1()

