import matplotlib.pyplot as plt
import numpy as np
n = int(input())
dataset = {f"experience{i}" : np.random.randn(100) for i in range(n)} 

def graphique(dataset) :
    nb_graph = len(dataset)
    x = np.arange(0,100, 1)
    plt.figure()
    for i in range(1,nb_graph+1) :
        plt.subplot(nb_graph, 1, i)
        plt.plot(x, dataset['experience{}'.format(i-1)])
        plt.title('experience{}'.format(i-1))
    plt.show()
        
        