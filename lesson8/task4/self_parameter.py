class Complex:
    def create(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part

class Calculator:
    current = 0
    def add(self, amount):
        self.current+=amount

    def get_current(self):
        return self.current

c1=Calculator()
print(c1.get_current())
c1.add(2)
print(c1.get_current())
c1.add(10)
print(c1.get_current())
