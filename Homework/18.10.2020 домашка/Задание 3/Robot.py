print("Введите первоночальное направление Киборг-убийцы ")
direct = int(input())
print(" Введите его дальнейшее действие")
N = int(input())
if (direct == 11 or direct == 14 or direct == 12 or direct == 13) and (N == 1 or N == 0 or N == -1):
    if direct == 11 and N == 0:
        print("Киборг-убица движется на север")
    if direct == 11 and N == 1:
        print("Киборг-убийца движется на запад")
    if direct == 11 and N == -1:
        print("Киборг-убийца движется на восток")
    if direct == 12 and N == 0:
         print("Киборг-убийца движется на запад")
    if direct == 12 and N == 1:
        print("Киборг-убийца движется на юг")
    if direct == 12 and N == -1:
        print("Киборг-убийца движется на север")
    if direct == 14 and N == 0:
         print("Киборг-убийца двжется на восток")
    if direct == 14 and N == 1:
         print("Киборг-убийца движется на север")
    if direct == 14 and N == -1:
        print("Киборг-убийца движется на юг")
    if direct == 13 and N == 0:
        print("Киборг-убийца движется на юг")
    if direct == 13 and N == 1:
        print("Киборг-убийца движется на восток")
    if direct == 13 and N == -1:
        print("Киборг-убийца движется на запад")
else:
    print(" Вы активировали охоту на секретные цели, Киборг-убица движется к вашему дому")