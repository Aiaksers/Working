# Дана строка. Если ее длина больше 10, то оставить в строке только первые 6 символов, иначе дополнить строку символами 'o' до длины 12.
str1 = input()
lp = len(str1)
if lp > 10:
    str1=str1[0:6]
    print(str1)
else:
    while len(str1) != 12:
        str1 = str1 + "o"

print(str1)

