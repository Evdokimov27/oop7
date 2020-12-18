import datetime

class vr:
    def vremy(self):
        now = datetime.datetime.now()
        now.strftime("%d-%m-%Y %H:%M")
        print('день: ', now.day)
        print('месяц:', now.month)
        print('год: ', now.year)

    def vremy2(self):
        now = datetime.datetime.now()
        now.strftime("%H:%M:%S")
        print('Час: ', now.hour)
        print('минута: ', now.minute)
        print('секунда: ', now.second)

    def vremy3(self):
        n = int(input("введите количество секунд: "))
        d = n // (24 * 3600)
        h = d // 24
        m = h // 60
        print('Кол-во дней:', d)
        print('Кол-во час:', h)
        print('Кол-во мин:', m)
        print('Кол-во сек:', n)

    def vremy4(self):
        def is_year_leap():
            year = int(input())
            if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
                print('True')
                return is_year_leap()
            else:
                print('False')
        is_year_leap()

t = vr()
x = int(input('Выберите действие: 1. дата 2. время 3. сек во времени 4. високосный год: '))
if x == 1:
    t.vremy()
elif x == 2:
    t.vremy2()
elif x == 3:
    t.vremy3()
elif x == 4:
    t.vremy4()