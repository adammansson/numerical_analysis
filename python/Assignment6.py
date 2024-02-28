import numpy as np

def Exercise1():
    A = np.array([[4, 0],
                  [3, 1]])

    Q, R = np.linalg.qr(A, 'complete')
    print(Q)
    print(R)

    print(Q @ R)

    my_Q = np.array([[4/5, -3/5],
                     [3/5, 4/5]])
    my_R = np.array([[5, 3/5],
                     [0, 4/5]])

    print(my_Q @ my_R)

def Exercise3():
    A = np.array([[0, 1],
                  [0, 0]])
    U, S, Vh = np.linalg.svd(A)
    print(U)
    print(S)
    print(Vh)

    my_U = np.array([[1, 0],
                     [0, 1]])
    my_S = np.array([[1, 0],
                     [0, 0]])
    my_Vh = np.array([[0, 1],
                     [1, 0]])

    print(my_U @ my_S @ my_Vh)

if __name__ == "__main__":
    # Exercise1()
    Exercise3()
