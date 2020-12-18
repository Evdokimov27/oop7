import random
class mas:
    def mass(self):
        a.mass()
    def clear(self):
        a.clear()
    def sort(self):
        a.sort()
    def delete(self):
        a.pop(3)
    def remove(self, x):
        a.remove(x)



m = mas()
a = []
n = int(input())
for b in range(n):
    a.append(random.randrange(1, 20))
print(a, "Массив размерностью", n)
x = int(input())

if  x == 1:
    c = []
    n = int(input())
    for b in range(n):
        c.append(random.randrange(1, 20))
    print(c)
    
elif x == 2:
    m.clear()
    print(a, "Массив отчищен")

elif x == 4:
    for c in range(len(a) - 1):
        for d in range(len(a) - 1):
            if a[d] < a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    print(a, "Сортировка по убыванию")
    for c in range(len(a) - 1):
        for d in range(len(a) - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    m.sort()
    print(a, "Сортировка по возрастанию")

elif x == 3:
    m.delete()
    print(a, "Элемент удален")

elif x == 5:
    i = int(input('Число, которое нужно убрать - '))
    m.remove(i)
    print(a)