import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
from QRFactorization import GramSchmidt

def exercise_1():
    xs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ys = [67052, 68008, 69803, 72024, 73400, 72063, 74669, 74487, 74065, 76777]

    ts = np.flip(np.polyfit(xs, ys, 3))
    p = Polynomial(ts)
    # print(p)

    ans = round(p(26))
    return ans

def exercise_2():
    A = np.array([[4, 2, 3, 0],
         [-2, 3, -1, 1],
         [1, 3, -4, 2],
         [1, 0, 1, -1],
         [3, 1, 3, -2]])

    _, norms = GramSchmidt(A)
    ans = round(norms[2], 4)
    # print(ans)

    # _, R = np.linalg.qr(A)
    # np_ans = R[2, 2]
    # print(np_ans)

    return ans

def exercise_3():
    xs = [1 + x * (3 / 11) for x in range(12)]
    d = 5
    ys = [sum([x**k for k in range(d + 1)]) for x in xs]

    A = np.array([[x**i for i in range(d + 1)] for x in xs])
    _, R = np.linalg.qr(A)

    # c = np.linalg.solve(R, Q.T @ ys)
    # print(c)

    ans = round(np.linalg.cond(R, 2))
    return ans

if __name__ == '__main__':
    print("Exercise 1:", exercise_1())
    print("Exercise 2:", exercise_2())
    print("Exercise 3:", exercise_3())