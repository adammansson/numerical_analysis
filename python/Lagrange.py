import numpy as np
import matplotlib.pyplot as plt

def LagrangePolynomial(i, xs):
    N = len(xs)
    res = np.polynomial.Polynomial([1])
    for k in range(N):
        if k != i:
            res *= (np.polynomial.Polynomial([0, 1]) - xs[k]) / (xs[i] - xs[k])

    return res

def LagrangeInterpolation(xs, ys):
    N = len(xs)
    res = np.polynomial.Polynomial([0])
    for i in range(N):
        res += ys[i] * LagrangePolynomial(i, xs)

    return res

def exercise_1():
    N = 20
    xs = [-1 + 2*i/N for i in range(N + 1)]
    f = lambda x : np.exp(-x**2)
    fs = [f(x) for x in xs]
    ys = [LagrangeInterpolation(xs, fs)(x) for x in xs]
    es = [abs(f(x) - LagrangeInterpolation(xs, fs)(x)) for x in xs]

    plt.plot(xs, ys)
    plt.show()

def exercise_2():
    xs = [1, 2, 3, 4, 5, 6]
    ys = [10, 10, 10, 10, 10, 15]
    p = LagrangeInterpolation(xs, ys)
    print(p(7))

if __name__ == "__main__":
    # exercise_1()
    exercise_2()

