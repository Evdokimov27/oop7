class math1:
    def plus(self):
        print(a + b, "- Сложение")

    def minus(self):
        print( a - b, "- Вычитание")

    def umnojenie(self):
        print(a * b, "- Умножение")

    def delenie(self):
        print(a / b, "- Деление")
a = int(input("Первое число - "))
b = int(input("Второе число - "))
matem = math1()
matem.plus()
matem.minus()
matem.umnojenie()
matem.delenie()

