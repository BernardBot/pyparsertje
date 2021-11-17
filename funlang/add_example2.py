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

    @classmethod
    def parser(cls):
        p = pyparsing_common.number
        p.setParseAction(cls.fromParseAction)
        return p

    @classmethod
    def parseString(cls, s):
        return cls.parser().parseString(s)[0]

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
    
    @classmethod
    def parser(cls):
        # this is now dynamically created
        # should be a field of this class
        # however we need access to 'cls' for the parseAction
        p = Num.parser() + Suppress("+") + Num.parser()
        p.setParseAction(cls.fromParseAction)
        return p

    @classmethod
    def parseString(cls, s):
        return cls.parser().parseString(s)[0]
        
p = Add.parseString("10 + -33.12")
print(p, "=", p.eval())

e0 = Num(10)
e1 = Num(20)
e2 = Add(e0, e1)

print(e2, "=", e2.eval())
