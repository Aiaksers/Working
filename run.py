r=10
plusRun=0
rs=10
d=0
dayNumber=int(input('Введите количество дней:'))
for i in range (9):
    plusRun=r*0.1
    r+=plusRun
    print('Пробег лыжника за',i+2,'день:',round(r,1))
r=10
plusRun=0
for i in range (6):
    plusRun=r*0.1
    r+=plusRun
    rs+=r
print('Сумма за 7 дней:',round(rs,1))
r=10
plusRun=0
rs=10
if dayNumber == 0:
    rs = 0
else:
    for i in range (dayNumber-1):
            plusRun=r*0.1
            r+=plusRun
            rs +=r
print('Сумма растояния которое пробежал лыжник за введённое количство дней:',round(rs,1))
rs=10
r=10
plusRun=0
while rs<80:
    plusRun = r * 0.1
    r += plusRun
    rs += r
    d +=1
print('Лыжнику не надо увеличивать пробег на',d,'день')
