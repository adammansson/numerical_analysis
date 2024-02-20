import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt

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

def assignment4_2():
    xs = [0, 2, 3]
    ys = [1, 3, 1]
    p = LagrangeInterpolation(xs, ys)

    xs_plot = np.linspace(0, 3, 100)
    ys_plot = [p(x) for x in xs_plot]

    print(p)
    plt.scatter(xs, ys)
    plt.plot(xs_plot, ys_plot)
    plt.show()

def assignment4_3():
    xs = [-1, 1, 2, 3]
    ys = [3, 1, 3, 7]

    p = LagrangeInterpolation(xs, ys)
    print(p)
    xs_plot = np.linspace(-1, 3, 100)
    ys_plot = [p(x) for x in xs_plot]

    plt.scatter(xs, ys)
    plt.plot(xs_plot, ys_plot)

    p = Polynomial([1, -1, 1]) + Polynomial([1]) * Polynomial([1, 1]) * Polynomial([-1, 1]) * Polynomial([-2, 1]) * Polynomial([-3, 1]) * Polynomial([0, 0, 1])
    print(p)
    ys_plot = [p(x) for x in xs_plot]
    plt.plot(xs_plot, ys_plot)
    plt.show()

def assignment4_4():
    s1 = 1 + (1/4) * Polynomial([-1, 1]) - (1/4) * (Polynomial([-1, 1]) ** 3)
    x1 = np.linspace(1, 2, 100)

    s2 = 1 + (-1/2) * Polynomial([-2, 1]) - (3/4) * (Polynomial([-2, 1]) ** 2) + (1/4) * (Polynomial([-2, 1]) ** 3)
    x2 = np.linspace(2, 3, 100)
    
    plt.plot(x1, [s1(x) for x in x1])
    plt.plot(x2, [s2(x) for x in x2])
    plt.scatter([1, 2, 3], [1, 1, 0])
    plt.show()

if __name__ == "__main__":
    # exercise_1()
    # exercise_2()
    # assignment4_2()
    # assignment4_3()
    assignment4_4()
