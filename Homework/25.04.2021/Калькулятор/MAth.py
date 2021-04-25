# Ввод:
# 1. 2 числа с клавиатуры
# 2. Знак операции с клавиатуры

# Основная цель:
# 1. Вычислить в соотвеьствии с вводом

# Побочные цели:
# 1. Получить числа
# 2. Проверить, являются ли числа числом
# 3. Получить знак операции
# 4. Проверить знак:
#   а) Если введен 0, программа заканчивается
#   б) Если введено что-либо не то, сообщение об ошибке и повторный ввод
# 5. Высчитать в соответствии с вводом
# 6. Повторять вечность
while True:
    stop=False
    while True:
        try:
            numberone = float(input('Введите первое число: '))
            break
        except ValueError:
                    print("Число не является числом")
                    break

    while True:
        try:
            numbertwo = float(input('Введите второе число: '))
            break
        except ValueError:
                    print("Число не является числом")
                    break

    simb=input("Введите знак действий ('+','-','*','/' или '0', если вы хотите выйти): ")
    if simb=='+':
        print('Результат: ', numberone+numbertwo)
    elif simb == '-':
        print('Результат: ', numberone - numbertwo)
    elif simb=='*':
        print('Результат: ', numberone * numbertwo)
    elif simb=='/':
        try:
            print('Результат: ', numberone / numbertwo)
        except ZeroDivisionError:
            print('Делить на ноль невозможно')
    elif numberone =="stop" or numbertwo=="stop":
                print('Программа остановлена')

                break
    else:
        print('Ввод не определен')
