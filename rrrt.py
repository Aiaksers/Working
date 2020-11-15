print("Дана строка. Если она начинается на abc ,то заменить их на www, иначе добавить в конец строки zzz.")

str1="zzz"
str = input("Введите строку")
if str[0:3]=="abc" :
    str=str.replace(str[0:3],"www")
else :
    str=str+str1
print(str)