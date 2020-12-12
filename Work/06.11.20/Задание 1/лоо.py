import random
someList = [random.randint(0, 100) for i in range(random.randint(5, 50))]

def printList(oneList):
    for elem in oneList:
        print(elem, end=' ')
    print()
def poiskList(oneList,finding):
    collich=0
    for i in range(len(oneList) - 1):
        for j in range(len(oneList) - 1):
            if oneList[i] == oneList[j]:
                finding+=1
                collich=j
            if collich != 0:
                print(collich, "-ый символ по счёту")

printList(someList)
poiskList(someList,0)
printList(someList)

def udalLIst(onelist):
    for i in range(len(oneList)):
        for j in range(len(oneList)):
            if i == j:
                oneList.remove(j)

    return


