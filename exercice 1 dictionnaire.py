classeur = {
    "positif" : [],
    "negatif" : []}

def trier(classeur, nombre) :
    if nombre >= 0 :
       classeur['positif'].append(nombre)
    else :
        classeur["negatif"].append(nombre)
    return classeur
    
