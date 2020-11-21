print ("Дана строка. Определите сколько раз символов '+' и '-' в ней. А так же сколько таких же символов, за которыми следует цифра 0.")
strok= input("Введите строку")
first = 0
second= 0
pam = 0
boynextdoor = 0
for i in range(len(strok) ):
    if str[i] == '+':
        first += 1
    if str[i] == '-':
        second += 1
    if str[i : i + 2] == "+0":
        pam += 1
    if str[i : i + 2] == "-0":
        boynextdoor += 1
print("В это строке ", first, " +")
print("В это строке ", second, " - ")
print("В это строке ", pam, " + после которы идёт 0")
print("В это строке ", boynextdoor, " - после которы идёт 0")

