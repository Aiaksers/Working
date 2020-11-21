import random
o = int(input("Введите количество раундов  "))
print('''
1. Ножницы;
2. Бумага;
3. Камень;
''')
comp = random.randint(1, 3)
compwin = 0
youwin = 0
unwin = 0

for t in range(o):
        you = int(input())
        if comp == you:
                unwin += 1
                print("нечья")
        if comp == 1 and you == 2:
                print("Компьютер выиграл")
                compwin += 1
        if comp == 1 and you == 3:
                youwin += 1
                print("Вы выиграли")
        if comp == 2 and you == 1:
                youwin += 1
                print("Вы победили")
        if comp == 2 and you == 3:
                compwin += 1
                print("Компьютер выиграл")
        if comp == 3 and you == 1:
                compwin += 1
                print("Компьютер выиграл")
        if comp == 3 and you == 2:
                youwin += 1
                print(" Вы выиграли ")
        elif (comp > 3 and comp < 1) and (you > 3 and you < 1):
                print("Глянь варианты выше))")
print('Счет бота:', compwin)
print('Ваш счет:', youwin)
if compwin > youwin:
        print('Вы проиграли')
elif compwin < youwin:
        print('Вы выиграли')
elif compwin == youwin:
        print('Ничья')


