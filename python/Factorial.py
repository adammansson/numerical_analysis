import numpy as np
import math
from numpy.polynomial import Polynomial

def LagrangePolynomial(i, xs):
    N = len(xs)
    res = np.polynomial.Polynomial([1])
    for k in range(N):
        if k != i:
            res *= (Polynomial([0, 1]) - xs[k]) / (xs[i] - xs[k])

    return res

def LagrangeInterpolation(xs, ys):
    N = len(xs)
    res = np.polynomial.Polynomial([0])
    for i in range(N):
        res += ys[i] * LagrangePolynomial(i, xs)

    return res

if __name__ == "__main__":
    xs = [x for x in range(0, 10)]
    ys = [math.factorial(x) for x in xs]

    P = LagrangeInterpolation(xs, ys)
    print(P(4.5))
