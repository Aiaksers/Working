from random import randint
str=input('Введите строку: ')
count=0
for i in range(len(str)):
    asciisymbol = randint(97, 122)
    str1=str[0:3]
    str2=str1[1:]
    if len(str2)>=1:
        str2=str2.replace(str2[0],chr(asciisymbol),1)
        str1=str1[0]+str2
        print(str1)
    if len(str1)==3:
        midsymbol=ord(str1[1])
        firstsymbol=ord(str1[0])
        lastsymbol=ord(str1[2])
        if midsymbol==firstsymbol or midsymbol==firstsymbol:
            asciisymbol = randint(97, 122)
            str2 = str1[1:]
            str2 = str2.replace(str2[0], chr(asciisymbol), 1)
            str1 = str1[0] + str2
    elif len(str1)==2:
        midsymbol=ord(str1[1])
        firstsymbol=ord(str1[0])
        if midsymbol==firstsymbol:
            asciisymbol = randint(97, 122)
            str2 = str1[1:]
            str2 = str2.replace(str2[0], chr(asciisymbol), 1)
            str1 = str1[0] + str2
    else:
        continue
    str=str[3:]