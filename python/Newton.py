import numpy as np

row0 = lambda x1, x2, x3: x1**2 - 2*x1 + x2**2 - x3 + 1
row1 = lambda x1, x2, x3: x1*x2**2 - x1 - 3*x2 + x2*x3 + 2
row2 = lambda x1, x2, x3: x1*x3**2 - 3*x3 + x2*x3**2 + x1*x2

row0_prime_1 = lambda x1, x2, x3: 2*x1 - 2
row0_prime_2 = lambda x1, x2, x3: 2*x2
row0_prime_3 = lambda x1, x2, x3: -1

row1_prime_1 = lambda x1, x2, x3: x2**2 - 1
row1_prime_2 = lambda x1, x2, x3: 2*x1*x2 - 3 + x3
row1_prime_3 = lambda x1, x2, x3: x2

row2_prime_1 = lambda x1, x2, x3: x3**2 + x2
row2_prime_2 = lambda x1, x2, x3: x3**2 + x1
row2_prime_3 = lambda x1, x2, x3: 2*x1*x3 - 3 + 2*x2*x3

f = lambda x1, x2, x3: np.array([row0(x1, x2, x3), row1(x1, x2, x3), row2(x1, x2, x3)])
Jf = lambda x1, x2, x3: np.matrix([[row0_prime_1(x1, x2, x3), row0_prime_2(x1, x2, x3), row0_prime_3(x1, x2, x3)],
                         [row1_prime_1(x1, x2, x3), row1_prime_2(x1, x2, x3), row1_prime_3(x1, x2, x3)],
                         [row2_prime_1(x1, x2, x3), row2_prime_2(x1, x2, x3), row2_prime_3(x1, x2, x3)],
                        ])

def Newton(f, Jf, x0, iterations):
    x = x0
    for _ in range(iterations):
        delta_x = np.linalg.solve(Jf(*x), -1 * f(*x))
        x = x + delta_x

    return x

def assignment3_1():
    r = np.array([1, 1, 1])
    x0 = np.array([1, 2, 3])

    x5 = Newton(f, Jf, x0, 5)
    x6 = Newton(f, Jf, x0, 6)
    e5 = np.linalg.norm(r - x5, 2)
    e6 = np.linalg.norm(r - x6, 2)
    print(e6 / e5)
    # CORRECT ANSWER: 0.2082

if __name__ == "__main__":
    assignment3_1()

