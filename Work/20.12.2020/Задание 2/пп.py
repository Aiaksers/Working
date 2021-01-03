import random

razmerkolodi=int(input("Введите размер колоды : "))
koloda=[random.randint(0,100)  for i in range(razmerkolodi)]
chast1koloda=[]
chast2koloda=[]
peremeshivanaaykaloda=[]
def printList(oneList):
    for elem in oneList:
        print(elem, end=' ')
    print()

def peremeshivanie (twoList):
    if len(twoList)%2==1:
        twoList.append(random.randint(0,100))
    for i in range(1,len(twoList)+1):
        if i ==len(twoList)/2:
            for j in range(0,i):
                chast1koloda.append(twoList[j])
            for k in range(i,len(twoList)):
                chast2koloda.append(twoList[k])
            chast1koloda.reverse()
            chast2koloda.reverse()
            twoList=[chast1koloda + chast2koloda for c in range(1) for d in range(1)]
    print(twoList)





printList(koloda)
peremeshivanie (koloda)