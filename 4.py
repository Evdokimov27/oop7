import random
a = []
n = 0
class massiv:
    n = 0
    def zap (self):
        if self.n == 0:
            g = int(input("Размерность массива - "))
            for i in range (g):
                a.append(random.randrange(1,10))
            self.n += 1
            print(a)
        else:
            print("Массив уже заполнен")
    def clear (self):
        if self.n != 0:
            a.clear()
            print("Массив отчищен")
            print(a)
            self.n -= 1
        else: 
            print("Массив уже отчищен")
    def pop (self):
        if self.n != 0:
            j = int(input("Индексы элемента - "))
            a.pop(j)
            print(a)
        else:
            print("Сначала нужно заполнить массив")
    def sort (self):
        u = int(input("1. По возрастанию, 2.По убыванию - "))
        if u == 1:
            for j in range (len(a)-1):
                for o in range (len(a)-1):
                    if a[o] > a [o+1]:
                        a[o], a[o+1] = a[o+1], a[o]
        if u == 2:
            for j in range (len(a)-1):
                for o in range (len(a)-1):
                    if a[o] < a [o+1]:
                        a[o+1], a[o] = a[o], a[o+1]
            print(a)
    def delete (self):
        v = int(input("Введите элемент - "))
        a.remove(v)
        print(a)
y = massiv()
while True:
    k = int(input("1.Заполнить, 2.Отчистить, 3.Удалить, 4.Сортировка, 5.Удалить - "))
    if k == 1:
        y.zap()
    if k == 2:
        y.clear()
    if k == 3:
        y.pop()
    if k == 4:
        y.sort()
    if k == 5:
        y.delete() 
