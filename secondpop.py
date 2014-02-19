file = open ('file.txt')
text = file.read()
nameDict = {}
first = (0,0,0)
second = (0,0,0)
for line in text.split('\n'):
    name, sex, freq = line.split (',')
    freq = int(freq)
    if sex == 'F':
        if freq > first[2]:
            second = first
            first = (name,sex,freq)
        elif freq> second[2]:
            second = (name,sex,freq)
print (second)


    
