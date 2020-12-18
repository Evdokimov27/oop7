class ur4:
    def pr1(self):
        import random
        a = []
        n = int(input())
        for b in range(n):
            a.append(random.randrange(1, 50))
        for c in range(len(a) - 1):
            for d in range(len(a) - 1):
                if a[d] < a[d + 1]:
                    a[d], a[d + 1] = a[d + 1], a[d]
        print(a)

    def pr2(self):
        import random
        a = [0]
        n = int(input())
        for b in range(n - 1):
            a.append(random.randrange(1, 50))
        print(a)
        k = len(a) // 2 + 1
        for i in range(len(a) - 1):
            for j in range(len(a) - 1):
                if a[j] < a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                if a[k] % 2 == 0:
                    a[j], a[k] = a[k], a[j]
        print(a)

    def pr3(self):
        import random
        a = [0]
        n = int(input())
        for b in range(n):
            a.append(random.randrange(1, 100))
        print(a)
        a.sort(key=lambda x: x if x % 2 != 1 else 1)
        k = len(a) // 2
        for i in range(len(a) - 1):
            for j in range(len(a) - 1):
                if a[j] == 0:
                    a[j], a[k] = a[k], a[j]
        print(a)

    def pr4(self):
        import random
        a = []
        n = int(input())
        for b in range(n):
            a.append(random.randrange(1, 100))
        print(a)

        for c in range(len(a) - 1):
            for d in range(len(a) - 1):
                if a[d] < a[d + 1]:
                    a[d], a[d + 1] = a[d + 1], a[d]
        print(a)
        a = list(filter(lambda x: not int(x) % 2, a))
        print(a[0])

    def pr5(self):
        import random
        a = []
        n = int(input())
        for b in range(n):
            a.append(random.randrange(1, 100))
        print(a)

        for c in range(len(a) - 1):
            for d in range(len(a) - 1):
                if a[d] < a[d + 1]:
                    a[d], a[d + 1] = a[d + 1], a[d]
        a1 = sum(a) // n
        h = []
        i = 0
        while i < len(a):
            if a1 > a[i]:
                h.append(a[i])
                del a[i]
            else:
                i += 1
        print("Ср.арифметическое: ", a1)
        print("Меньше ср.арифметического: ", h)

    def pr6(self):
        import random
        a = []
        n = int(input())
        for b in range(n):
            a.append(random.randrange(1, 100))
        print(a)
        a.pop(0)
        a.pop(n - 2)
        print("Массив без мин. и макс. значений:", a)
        print("Сумма масива:", sum(a))

    def pr7(self):
        import random
        a = []
        list = [1, 2, 3, 5, 7, 11, 13, 17]
        for i in range(4):
            b = []
            for j in range(10):
                b.append(random.choice(list))
            a.append(b)
        print(a)

    def pr8(self):
        a = []
        for i in range(6):
            b = []
            for j in range(10):
                if i % 2 == 0:
                    for c in range(1, 6):
                        if len(b) == 10:
                            break
                        b.append(c)
                else:
                    for c in range(10, 0, -1):
                        if len(b) == 10:
                            break
                        b.append(c)
            a.append(b)
        print(a)

    def pr9(self):
        import random
        a = []
        for i in range(34):
            b = []
            for j in range(34):
                b.append(random.randrange(1, 10))
            a.append(b)
        a.sort(key=lambda x: x if x % 2 != 1 else 1)
        k = len(a) // 2
        for h in range(len(a) - 1):
            for n in range(len(a) - 1):
                if a[h] == 0:
                    a[h], a[k] = a[k], a[h]
        print(a)

    def pr10(self):
        print('не сделал!')

    def pr11(self):
        print('не сделал!')

    def pr12(self):
        import random
        a = []
        c = []
        d = []
        for i in range(5):
            b = []
            for j in range(5):
                b.append(random.randrange(1, 101))
            a.append(b)

            d.append(min(b))
            c.append(max(b))
        print(a)
        print(c, "- макс. среди каждой матрицы")
        print(d, "- мин. среди каждой матрицы")

uroven4 = ur4()
x = int(input())
if x == 1:
    uroven4.pr1()
elif x == 2:
    uroven4.pr2()
elif x == 3:
    uroven4.pr3()
elif x == 4:
    uroven4.pr4()
elif x == 5:
    uroven44.pr5()
elif x == 6:
    uroven4.pr6()
elif x == 7:
    uroven4.pr7()
elif x == 8:
    uroven4.pr8()
elif x == 9:
    uroven4.pr9()
elif x == 10:
    uroven4.pr10()
elif x == 11:
    uroven44.pr11()
elif x == 12:
    uroven4.pr12()
uroven4.pr1()
