import random
class table:
    def mat(self):
        self.a = []

    def mas(self):
        for i in range(4):
            self.b = []
            self.mas1()
            self.a.append(self.b)

    def mas1(self):
        for j in range(5):
            self.b.append(random.randrange(1, 10))

    def vivod(self):
        print(self.a[0])
        print(self.a[1])
        print(self.a[2])
        print(self.a[3])

    def all(self):
        self.mat()
        self.mas()
        self.vivod()

t = table()
t.all()
