#Create a dict where keys are numbers from 0 to -20 and associated values are the square of their keys
dico = {k : v for k, v in zip(range(0, -21, -1),[i**2 for i in range(0, -21, -1)]) 
} 