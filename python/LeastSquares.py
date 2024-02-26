import numpy as np
import math

def LeastSquares(data, fs):
    xss = [point[0] for point in data]
    ys = [point[1] for point in data]

    A = np.matrix([[f(xs) for f in fs] for xs in xss])
    rhs = A.T * A

    assert np.linalg.det(rhs) != 0

    b = np.array([ys]).T
    lhs = A.T * b

    return np.linalg.solve(rhs, lhs)

def exercise5_2b():
    data = [([0], 1), ([1], 2), ([3], 3)]
    fs = [lambda xs : 1, lambda xs : xs[0]]
    print(LeastSquares(data, fs))

def exercise5_2c():
    data = [([0, 1], 3), ([0, 1], 2), ([1, 0], 3), ([1, 0], 4), ([1, 2], 6)]
    fs = [lambda xs : 1, lambda xs : xs[0], lambda xs : xs[1]]
    print(LeastSquares(data, fs))

def P(x):
    if -math.pi < x < math.pi:
        return x / 2
    elif math.pi < x < 3*math.pi:
        return (x - 2*math.pi) / 2
    else:
        return 0

def exercise5_2d():
    m = 8
    xs = [-math.pi + ((i - 1) / m)*2*math.pi for i in range(1, m + 1)]
    ys = [P(x) for x in xs]
    data = [([x], y) for x in xs for y in ys]
    fs = [
        lambda xs : math.sin(xs[0]),
        lambda xs : math.sin(2 * xs[0]),
        lambda xs : math.sin(3 * xs[0]),
    ] 
    print(LeastSquares(data, fs))

if __name__ == "__main__":
    exercise5_2d()