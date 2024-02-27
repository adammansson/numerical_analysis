import numpy as np

def PowerMethod(A, x, k):
    for _ in range(k):
        u = x / np.linalg.norm(x, 2)
        x = A @ u
        lam = u.T @ x
    return lam, x / np.linalg.norm(x, 2)

def InversePowerMethod(A, x, s, k):
    As = A - s * np.identity(np.shape(A)[0])

    for _ in range(k):
        u = x / np.linalg.norm(x, 2)
        x = np.linalg.solve(As, u)
        lam = u.T @ x
    return 1 / lam + s, x / np.linalg.norm(x, 2)

def QRMethod(A, k):
    Q = np.identity(np.shape(A)[0])
    Qprod = np.identity(np.shape(A)[0])
    A = Q.T @ A @ Q

    for _ in range(k):
        Q, R = np.linalg.qr(A)
        Qprod = Qprod @ Q
        A = R @ Q

    return A, Qprod

def Exercise6_4():
    Aex1 = np.array([[5, 2, 2],
                   [2, 2, 0],
                   [2, 0, 0]])

    res = QRMethod(Aex1, 100)
    print("Aex1: ")
    print(res[0])
    print(res[1])

    Aex2 = np.array([[2, 3, 4, 5],
                     [1, 0, 2, 3],
                     [0, 3, 4, 1],
                     [-1, 2, 3, -4]])

    res = QRMethod(Aex2, 500)
    print("Aex2: ")
    print(res[0])
    print(np.diagonal(res[0]))
    print(res[1])

if __name__ == "__main__":
    # A1 = np.array([[1, 2],
    #                [2, 1]])
    # x1 = np.array([1, 0])
    #
    # A2 = np.array([[1, 4],
    #                [-4, 1]])
    # x2 = np.array([1, 0])

    # print("A1: ", PowerMethod(A1, x1, 100), InversePowerMethod(A1, x1, 4, 100))
    # print("A2: ", PowerMethod(A2, x2, 100), InversePowerMethod(A2, x2, 0, 100))

    Exercise6_4()

