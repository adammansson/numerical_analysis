import numpy as np

A = [[3, 1, -1],
     [2, 4, 1],
     [-1, 2, 5]]

B = [[1, 1.0001],
     [1.0001, 1]]

C = [[1.0001, 1],
     [1, 1.0001]]

if __name__ == "__main__":
    print("cond A = ", np.linalg.cond(A))
    print("cond B = ", np.linalg.cond(B))
    print("cond C = ", np.linalg.cond(C))

