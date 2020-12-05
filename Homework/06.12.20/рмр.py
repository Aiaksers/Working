str = input('Введите строку, где одно слово является обращением другого: ')
raz=0
for i in str:
    if i != ' ':
        raz+=1
    else:
        word=str[:raz]
        word=word[::-1]
        str=str[raz+1:]
        raz = 0
        str2 = str
        for i in str:
            if i != ' ':
                raz += 1
            else:
                if str2.startswith(' '):
                    str2 = str2[1:]
                else:
                    str2 = str
                word2 = str2[:raz]
                str2=str2[raz:]
                count = 0
                if word==word2:
                    print(word[::-1],word2)
                    word=''
                    word2=''
                else:
                    word2=''