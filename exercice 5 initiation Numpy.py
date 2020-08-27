import numpy as np 
def initialisation(n, p) :
    # n nombre de lignes
    # p nombre de colonnes 
    # créer une matrice aléatoire de taille (n, p+1) dont la p+1-ième colones est faite de 1
    return np.concatenate((np.random.randn(n,p), np.ones((n,1))), axis=1)
