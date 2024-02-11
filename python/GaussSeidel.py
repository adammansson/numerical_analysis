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

if __name__ == "__main__":
    assignment3_3()

