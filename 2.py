class pila:
    hp = 100
    def cut(self, a):
        if self.hp != 5:
            print(a)

    def kill(self, a):
        self.hp -= 1
        print(a)

    def legat(self, a):
        print(a)
k = pila()
k.cut('Пилить')
k.kill('Прочность %:')
print(k.hp)
k.legat('Сломалась')