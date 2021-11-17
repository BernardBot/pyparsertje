from pyparsing import *

class Num():
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def eval(self):
        return self.num

    @classmethod
    def fromParseAction(cls, s, loc, toks):
        return cls(*toks)

class Add():
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def __str__(self):
        return str(self.e1) + " + " + str(self.e2)

    def eval(self):
        return self.e1.eval() + self.e2.eval()

    @classmethod
    def fromParseAction(cls, s, loc, toks):
        return cls(*toks)

num = pyparsing_common.number
add = num + Suppress("+") + num

# do not want to write this!
#num.setParseAction(Num.fromParseAction)
#add.setParseAction(Add.fromParseAction)

p = add.parseString("10 + 20")
print(p) # this is a list
print(p[0], "=", p[0].eval())

e0 = Num(10)
e1 = Num(20)
e2 = Add(e0, e1)
e3 = Add(e2, e2)

print(e2, "=", e2.eval())
print(e3, "=", e3.eval())
