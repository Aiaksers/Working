import random

someList = [random.randint(0, 100) for i in range(random.randint(5, 50))]

def printList(oneList):
    for elem in oneList:
        print(elem, end=' ')
    print()

def sortList(oneList):
    for i in range(len(oneList) - 1):
        for j in range(len(oneList) - 1):
            if oneList[j] > oneList[j + 1]:
                buf = oneList[j + 1]
                oneList[j + 1] = oneList[j]
                oneList[j] = buf

printList(someList)
sortList(someList)
printList(someList)