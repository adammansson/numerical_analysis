import numpy as np

def GramSchmidt(A):
    # A = np.append(A.T, [1, 0, 0]).reshape(3, 3).T

    _, cols = np.shape(A)
    Q = []
    norms = []

    v1 = A[:, 0]
    y1 = v1
    norm = np.linalg.norm(y1)
    q1 = y1 / norm
    Q.append(q1)
    norms.append(norm)

    for i in range(1, cols):
        vi = A[:, i]
        yi = vi

        for j in range(1, i + 1):
            yi = np.subtract(yi, np.dot(Q[j - 1], np.dot(Q[j - 1], vi)))

        norm = np.linalg.norm(yi)
        qi = yi / norm
        Q.append(qi)
        norms.append(norm)

    return np.matrix(Q).T, norms

def QRDecomposition(A):
    rows, cols = np.shape(A)
    Q, norms = GramSchmidt(A)
    print(Q)
    R = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            if i == j:
                R[i, i] = norms[i]
            if j > i:
                qi = Q[:, i - 1]
                print(qi.reshape(1, 3))
                vj = np.array(A[:, j - 1])
                print(vj.T)
                r = np.dot(qi, vj.T)
                print(r)
                R[i, j] = r

    return Q, R

if __name__ == "__main__":
    A = np.array([[-4, -4],
                   [-2, 7],
                   [4, -5]])
    print(QRDecomposition(A))