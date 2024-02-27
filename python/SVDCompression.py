import numpy as np
from PIL import Image, ImageOps
from math import prod

def ImageToMatrix(img):
    return np.array([[e / 255 for e in row] for row in np.array(img)])

def MatrixToImage(A):
    return Image.fromarray(np.array([[e * 255 for e in row] for row in A]))

def CompressMatrix(A, r):
    size_A = prod(np.shape(A))

    U, S, Vh = np.linalg.svd(A)

    new_U = U[:, 0:r] 
    new_S = np.diag(S[0:r])
    new_Vh = Vh[0:r]

    size_U = prod(np.shape(new_U))
    size_S = prod(np.shape(new_S))
    size_Vh = prod(np.shape(new_Vh))
    size_sum = size_U + size_S + size_Vh

    return new_U @ new_S @ new_Vh, size_sum / size_A

def Exercise6_6():
    img = ImageOps.grayscale(Image.open("beach_nz.png"))
    A = ImageToMatrix(img)

    Ac, r = CompressMatrix(A, 50)
    print(r)

    imgc = MatrixToImage(Ac)
    imgc.show()

if __name__ == "__main__":
    Exercise6_6()
