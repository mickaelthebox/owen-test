#the goal is to save on python all the contains of the files from a repertory. However, you must enable people to access these contains with the name of the files
from glob import glob
def list_of_txt(file) :
    with open('{}'.format(file)) as f :
        return f.read().splitlines()
txt_names = glob('*.txt')
dict_files = {
    name : list_of_txt(name) for name in txt_names }
    
