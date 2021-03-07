class pokupatel:
    def __init__(self):
        name = 'Имя: '+input('Введите имя: ')
        surname = 'Фамилия: '+input('Введите фамилию: ')
        lastname = 'Отчество: '+input('Введите отчество: ')
        cardnumber = 'Номер карты: '+input('Введите номер кредитной карточки: ')
        banknumber = 'Номер банковского счета: '+input('Введите номер банковского счета: ')
        self.pokupatel=[name,surname,lastname,cardnumber,banknumber]

    def setAttribute(self):
        attrnum=int(input('''Введите номер критерия,который желаете изменить
                          (1-имя,
                          2-фамилия,
                          3-отчество,
                          4-номер карточки,
                          5-номер банковского счета): '''))
        newattr=input('Введите новое значение критерия: ')
        if attrnum==1:
            self.pokupatel[attrnum-1]='Имя: '+ newattr
        elif attrnum==2:
            self.pokupatel[attrnum-1] = 'Фамилия: '+ newattr
        elif attrnum==3:
            self.pokupatel[attrnum-1] = 'Отчество: '+newattr
        elif attrnum==4:
            self.pokupatel[attrnum-1] = 'Номер карты: '+newattr
        elif attrnum==5:
            self.pokupatel[attrnum-1] = 'Номер банковского счета: '+newattr
        else:
            print('Такой номер не найден')

    def seeAttributes(self):
        for i in range(5):
            print(self.pokupatel[i])