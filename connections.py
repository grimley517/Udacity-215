import csv

comics = {}
characters = {}

def addChar(Char, com, characters):
    if Char not in characters:
        characters[Char] = []
    characters[Char].append(com)
    return characters
    
def addCom(Char, com, comics):
    if com not in comics:
        comics[com] = []
    comics[com].append(Char)
    return comics
    
tsv = csv.reader(open ('marvgraph'), delimiter = '\t')

for (char, com) in tsv:
    characters = addChar(char, com, characters)
    comics = addCom (char, com, comics)
print (comics)
input()
