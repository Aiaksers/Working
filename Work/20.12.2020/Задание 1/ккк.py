import random
class Ocher:
    def __init__(self):
        self._Ocher = []
    def push (self,nlo):
        self._Ocher.append(nlo)
    def pop(self):
        try:
            return self._Ocher.pop(0)
        except IndexError:
            print("No data")
    def peek(self):
        try:
            print(self._Ocher[len(self._Ocher)-1])
        except IndexError:
            print("No data")
    def firstnlo(self):
        try:
            print(self._Ocher[0])
        except IndexError:
            print("No data")

    def count(self):
        return len(self._Ocher)
someOcher=Ocher()

for i in range(random.randint(5,50)):
    someOcher.push(random.randint(0,100))

for i in range(someOcher.count()):
    print(someOcher.pop(), end=" ")
print()
print(someOcher.firstnlo())