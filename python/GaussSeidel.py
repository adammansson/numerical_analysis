import numpy as np

def GaussSeidel(A, b, x0, iterations):
    n = len(b)
    x = x0
    for _ in range(iterations):
        prev_x = x
        for row in range(n):
            sum = b[row]
            for col in range(n):
                if col > row:
                    sum -= A[row][col] * prev_x[col]
                elif col < row:
                    sum -= A[row][col] * x[col]

            x[row] = sum / A[row][row]

    return x

def assignment3_3():
    A = [[15, -5, 1, 1.1],
         [0, 5, 2, -1],
         [2, -1, 9, -1],
         [1, 1.1, -1, -6]]

    b = [1, 1, 1, 1]
    x0 = [2, 1, 1, 1]

    x10 = GaussSeidel(A, b, x0, 10)
    print(x10)
    print(np.linalg.norm(x10, 2))
    # CORRECT ANSWER: 0.2423

def exercise3_5():
    A = [[3, 1, -1],
         [2, 4, 1],
         [-1, 2, 5]]
    a_ans= [4, 1, 1]

    x100 = GaussSeidel(A, a_ans, [0, 10000, 0], 100)
    print(x100)
    print(np.matmul(A, x100))

    B = [[1, 1.0001],
         [1.0001, 1]]
    b_ans = [2, 3]
    x100 = GaussSeidel(B, b_ans, [0, 0], 100000)
    print(x100)
    print(np.matmul(B, x100))

    C = [[1.0001, 1],
         [1, 1.0001]]
    c_ans = [2, 3]
    x100 = GaussSeidel(C, c_ans, [0, 0], 100000)
    print(x100)
    print(np.matmul(C, x100))


if __name__ == "__main__":
    # assignment3_3()
    exercise3_5()

