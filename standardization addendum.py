import numpy as np
def standardization2(A):
    #A : numpy.ndarray
    return (A - A.mean(axis=0))/A.std(axis=0)
    