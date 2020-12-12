str=input("Введите строку из слов : ")+" "

word=" "
start=0
mem=0
invers=" "

other=""
start2=0
mem2=0

cup=0

for i in range(len(str)):
    if str[i]==" "  :
        mem =i
        word=word.replace(word,str[start:mem])
        invers=word.replace(word,word[::-1])
        start = i+1
        for j in range(len(str)):
            if str [j] == " "  :
                mem2 = j
                other = other.replace(other,str[start2:mem2])
                start2 = j+1
            if invers==other :
                cup+=1
                print("есть такая пара слов - " + word + " и " + other)

print("таких пар "+cup+" штук")
