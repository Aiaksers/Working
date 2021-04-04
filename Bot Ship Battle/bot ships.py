import random
class field:
    def __init__(self,size):
        global globalsize
        globalsize = size
        global field
        field = []
        for i in range(globalsize):
            field.append([])
            for j in range(globalsize):
                field[i].append('  ')

    def printfield(self):
        lettercounter = 65
        print('  ', end='  ')
        for i in range(globalsize):
            print(chr(lettercounter), end='  ')
            lettercounter += 1
        print()
        for i in range(globalsize):
            if i > 8:
                print(i + 1, end=' ')
            else:
                print(i + 1, end='  ')
            for j in range(globalsize):
                print(field[i][j], end=' ')
            print()

    def deletezeroes(self):
        for i in range(globalsize):
            for j in range(globalsize):
                if field[i][j] == ' ' + str(0):
                    field[i][j] = '  '

    def findfreespot(self):
        while True:
            global coordx
            global coordy
            coordy = random.randint(0, globalsize - 1)
            coordx = random.randint(0, globalsize - 1)
            if field[coordy][coordx] == ' ' + str(0) or field[coordy][coordx] == ' ' + str(1):
                pass
            else:
                break

    def addforship(self):
        global coordx
        global coordy
        fourship = 4
        while fourship != 0:
            prob = random.randint(1, 4)
            if prob == 1:
                coordy -= 1
                if coordy < 0:
                    coordy += 1
                else:
                    if field[coordy][coordx] == ' ' + str(1):
                        coordy += 1
                    else:
                        field[coordy][coordx] = ' ' + str(1)
                        fourship -= 1
            if prob == 2:
                try:
                    coordx += 1
                    if field[coordy][coordx] == ' ' + str(1):
                        coordx -= 1
                    else:
                        field[coordy][coordx] = ' ' + str(1)
                        fourship -= 1
                except IndexError:
                    coordx -= 1
            if prob == 3:
                try:
                    coordy += 1
                    if field[coordy][coordx] == ' ' + str(1):
                        coordy -= 1
                    else:
                        field[coordy][coordx] = ' ' + str(1)
                        fourship -= 1
                except IndexError:
                    coordy -= 1
            if prob == 4:
                coordx -= 1
                if coordx < 0:
                    coordx += 1
                else:
                    if field[coordy][coordx] == ' ' + str(1):
                        coordx += 1
                    else:
                        field[coordy][coordx] = ' ' + str(1)
                        fourship -= 1

    def addzeroes(self):
        for i in range(0, globalsize):
            for j in range(0, globalsize):
                if field[i][j] == ' ' + str(1):

                    if i - 1 >= 0:
                        if field[i - 1][j] == '  ':
                            field[i - 1][j] = ' ' + str(0)

                    try:
                        if field[i + 1][j] == '  ':
                            field[i + 1][j] = ' ' + str(0)
                    except IndexError:
                        pass

                    if j - 1 >= 0:
                        if field[i][j - 1] == '  ':
                            field[i][j - 1] = ' ' + str(0)

                    try:
                        if field[i][j + 1] == '  ':
                            field[i][j + 1] = ' ' + str(0)
                    except IndexError:
                        pass

                    try:
                        if field[i + 1][j + 1] == '  ':
                            field[i + 1][j + 1] = ' ' + str(0)
                    except IndexError:
                        pass

                    if j - 1 >= 0 and i - 1 >= 0:
                        if field[i - 1][j - 1] == '  ':
                            field[i - 1][j - 1] = ' ' + str(0)

                    try:
                        if j + 1 >= 0 and i - 1 >= 0:
                            if field[i - 1][j + 1] == '  ':
                                field[i - 1][j + 1] = ' ' + str(0)
                    except IndexError:
                        pass

                    try:
                        if j - 1 >= 0 and i + 1 >= 0:
                            if field[i + 1][j - 1] == '  ':
                                field[i + 1][j - 1] = ' ' + str(0)
                    except IndexError:
                        pass

    def addthreeship(self):
        global coordx
        global coordy
        threeship = 3

        while threeship!=0:
                prob = random.randint(1, 4)
                if prob == 1:
                    coordy -= 1
                    if coordy < 0:
                        coordy += 1
                    else:
                        if field[coordy][coordx] == ' ' + str(1) or field[coordy][coordx] == ' ' + str(0):
                            coordy += 1
                        else:
                            field[coordy][coordx] = ' ' + str(1)
                            threeship -= 1
                if prob == 2:
                    try:
                        coordx += 1
                        if field[coordy][coordx] == ' ' + str(1) or field[coordy][coordx] == ' ' + str(0):
                            coordx -= 1
                        else:
                            field[coordy][coordx] = ' ' + str(1)
                            threeship -= 1
                    except IndexError:
                        coordx -= 1
                if prob == 3:
                    try:
                        coordy += 1
                        if field[coordy][coordx] == ' ' + str(1) or field[coordy][coordx] == ' ' + str(0):
                            coordy -= 1
                        else:
                            field[coordy][coordx] = ' ' + str(1)
                            threeship -= 1
                    except IndexError:
                        coordy -= 1
                if prob == 4:
                    coordx -= 1
                    if coordx < 0:
                        coordx += 1
                    else:
                        if field[coordy][coordx] == ' ' + str(1) or field[coordy][coordx] == ' ' + str(0):
                            coordx += 1
                        else:
                            field[coordy][coordx] = ' ' + str(1)
                            threeship -= 1

    def addTwoship(self):
        global coordx
        global coordy
        twoship = 2
        while twoship!=0:
                prob = random.randint(1, 4)
                if prob == 1:
                    coordy -= 1
                    if coordy < 0:
                        coordy += 1
                    else:
                        if field[coordy][coordx] == ' ' + str(1) or field[coordy][coordx] == ' ' + str(0):
                            coordy += 1
                        else:
                            field[coordy][coordx] = ' ' + str(1)
                            twoship -= 1
                if prob == 2:
                    try:
                        coordx += 1
                        if field[coordy][coordx] == ' ' + str(1) or field[coordy][coordx] == ' ' + str(0):
                            coordx -= 1
                        else:
                            field[coordy][coordx] = ' ' + str(1)
                            twoship -= 1
                    except IndexError:
                        coordx -= 1
                if prob == 3:
                    try:
                        coordy += 1
                        if field[coordy][coordx] == ' ' + str(1) or field[coordy][coordx] == ' ' + str(0):
                            coordy -= 1
                        else:
                            field[coordy][coordx] = ' ' + str(1)
                            twoship -= 1
                    except IndexError:
                        coordy -= 1
                if prob == 4:
                    coordx -= 1
                    if coordx < 0:
                        coordx += 1
                    else:
                        if field[coordy][coordx] == ' ' + str(1) or field[coordy][coordx] == ' ' + str(0):
                            coordx += 1
                        else:
                            field[coordy][coordx] = ' ' + str(1)
                            twoship -= 1

    def addOneship(self):
        field[coordy][coordx] = ' ' + str(1)