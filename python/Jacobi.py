import numpy as np

def Jacobi(A, b, x0, iterations):
    n = len(b)
    x = x0
    for _ in range(iterations):
        prev_x = x
        for row in range(n):
            sum = b[row]
            for col in range(n):
                if col != row:
                    sum -= A[row][col] * prev_x[col]
            x[row] = sum / A[row][row]

    return x

def assignment3_3():
    A = [[3, 1, 1, 0],
         [1, 6, 3, -1],
         [6, 0, 9, -2],
         [1, 0, -1, -7]]

    b = [1, 1, 1, 1]
    x0 = [0, 1, 1, 0]

    x25 = Jacobi(A, b, x0, 25)
    print(x25)
    print(np.linalg.norm(x25, 2))
    # CORRECT ANSWER: 0.3857

if __name__ == "__main__":
    assignment3_3()

