import numpy as np

def matrix_transpose(A):
    A = np.array(A)
    N, M = A.shape
    result = np.zeros((M, N))
    for i in range(N):
        for j in range(M):
            result[j][i] = A[i][j]
    return result