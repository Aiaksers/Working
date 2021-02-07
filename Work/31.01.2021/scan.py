from collections import Counter
with open('pwd.txt') as f:
    myList = [ line.split(';') for line in f ]

flatList = [item for sublist in myList for item in sublist]
del flatList[0]

topPasswords=[0,0,0,0,0,0,0,0,0,0]
passwordnumber=0

for i in range(len(flatList)):
    try:
        if flatList[i][-1]!='n':
            del flatList[i]
    except IndexError:
        pass


for i in range(len(flatList)):
    try:
        flatList[i]=flatList[i][0:-1]
    except IndexError:
        pass

passOften = Counter(flatList).most_common(10)
oftenpasswords=[]
for i in range(10):
    oftenpasswords.append(passOften[i])
for i in range(10):
    print(i+1,'. ',oftenpasswords[i][0],' (',oftenpasswords[i][1],' раз)',sep='')