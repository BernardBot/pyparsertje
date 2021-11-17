from pyparsing import *

class Suffix():
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def eval(self):
        return self.num

    @classmethod
    def fromParseAction(cls, s, loc, toks):
        return cls(*toks)

word = Word(alphas)
suffix = Optional(word) + "." + Optional(word)

suffix.setParseAction(Suffix.fromParseAction)

p = add.parseString("10 + 20")
print(p) # this is a list
print(p[0], "=", p[0].eval())

e0 = Num(10)
e1 = Num(20)
e2 = Add(e0, e1)

print(e2, "=", e2.eval())
