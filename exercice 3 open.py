cd C:\Users\VulcomX\Desktop\programmation\Machine learning\owen-test
with open('fichier.txt', 'w') as f :
    for i in range(10) :
        f.write("{}^2 = {} \n".format(i, i**2))
        
file = "fichier.txt"

def list_of_txt(file) :
#créer une liste dans lequel chaque élément est une ligne du texte en entrée
#le but est de coder soi même readlines
    l = []
    with open('{}'.format(file),'r') as f :
        text = f.read()
        line = ''
        for i in range(len(text)) :
            if text[i] != '\n' :
                line += text[i]
            else : 
                l.append(line)
                line = ''
    return l

