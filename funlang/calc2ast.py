from pyparsing import *
import operator

# speed
ParserElement.enablePackrat()

# not really necessary... (is necessary for typing)
class Exp():
    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        return str(self.exp)

    @classmethod
    def fromParseAction(cls, s, loc, toks):
        return cls(*toks)

    def eval(self):
        return self.exp.eval()

class UnOp(Exp):
    ops = {
        "-" : operator.neg,
    }

    def __init__(self, op, e1):
        self.op = op
        self.e1 = e1

    def __str__(self):
        return self.op + str(self.e1)

    @classmethod
    def fromParseAction(cls, s, loc, toks):
        return cls(*(toks[0]))

    def eval(self):
        return self.ops[self.op](self.e1.eval())

class BinOp(Exp):
    ops = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv,
        "^" : operator.pow,
    }

    def __init__(self, e1, op, e2):
        self.e1 = e1
        self.op = op
        self.e2 = e2

    def __str__(self):
        return "(" + str(self.e1) + " " + self.op + " " + str(self.e2) + ")"

    @classmethod
    def fromParseAction(cls, s, loc, toks):
        e1, *toks = toks[0]
        while toks:
            op, e2, *toks = toks
            e1 = BinOp(e1, op, e2)
        return e1

    def eval(self):
        return self.ops[self.op](self.e1.eval(), self.e2.eval())

class Num(Exp):
    def eval(self):
        return self.exp

num = pyparsing_common.number
exp = infixNotation(num, [
    ("-", 1, opAssoc.RIGHT, UnOp.fromParseAction),
    ("^", 2, opAssoc.RIGHT, BinOp.fromParseAction),
    ("*", 2, opAssoc.LEFT, BinOp.fromParseAction),
    ("/", 2, opAssoc.LEFT, BinOp.fromParseAction),
    ("+", 2, opAssoc.LEFT, BinOp.fromParseAction),
    ("-", 2, opAssoc.LEFT, BinOp.fromParseAction),
])

num.setParseAction(Num.fromParseAction)
exp.setParseAction(Exp.fromParseAction)

p = exp.parseString("2 ^ (5 + 5) / 32")
print(p)
print(p[0])
print(p[0].eval())
