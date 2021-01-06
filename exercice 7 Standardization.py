import numpy as np
def standardization(A) :
    #A np.ndarray
    #standardiser chaque colonnes (preparation aux travaux de dataset)
    B = np.ones(A.shape)
    moyenne = A.mean(axis=0)
    sigma = A.std(axis=0)
    for j in range(A.shape[1]) :
        for i in range(A.shape[0]) :
            B[i,j] = (A[i,j] - moyenne[j])/sigma[j]
    return B
    