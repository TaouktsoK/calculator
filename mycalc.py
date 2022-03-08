import math


class Mycalc:
    def __init__(self, *args):
        for arg in args:
            self.num1 = float(args[0])
            if len(args) > 1:
                self.num2 = float(args[1])

    def add(self):
        res = self.num1 + self.num2
        return res

    def sub(self):
        res = self.num1 - self.num2
        return res

    def mult(self):
        res = self.num1 * self.num2
        return res

    def div(self):
        res = self.num1 / self.num2
        return res

    def sin(self):
        res = math.sin(self.num1*(math.pi/180))
        return res

    def cos(self):
        res = math.cos(self.num1*(math.pi/180))
        return res

    def tan(self):
        res = math.tan(self.num1*(math.pi/180))
        return res

    def log(self):
        res = math.log(self.num1, 10)
        return res

    def ln(self):
        res = math.log(self.num1, math.e)
        return res
