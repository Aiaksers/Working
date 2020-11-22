str1 = input()
y=len(str1)
for o in range(0,y,2):
        if str1[o] != "a":
                str1 = str1.replace(str1[o], "a")
                print(str1)
        elif str1[o] != "b":
                str1 = str1.replace(str1[o], "a")
        elif str1[o] == "a" and str1[o] == "b" :
                str1 = str1.replace(str1[o], "c")
                print(str1)






