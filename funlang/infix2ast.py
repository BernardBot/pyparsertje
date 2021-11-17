from pyparsing import *

class A():
    def __init__(self, e1, op, e2):
        self.e1 = e1
        self.op = op
        self.e2 = e2
    def __str__(self):
        return "(" + str(self.e1) + " " + self.op + " " + str(self.e2) + ")"

class B():
    def __init__(self, op, e1):
        self.op = op
        self.e1 = e1

    def __str__(self):
        return self.op + str(self.e1)

def foo(s, loc, toks):
    e1, op, e2 = toks[0][:3]
    a = A(e1, op, e2)
    for t in toks[0][3:]:
        if type(t) == int:
            a = A(a, op, t)
    return a

def baz(toks):
    e1, *toks = toks
    while toks:
        op, e2, *toks = toks
        e1 = A(e1, op, e2)
    return e1

def bar(s, loc, toks):
    op, e1 = toks[0]
    return B(op, e1)


num = pyparsing_common.number
exp = infixNotation(num, [
    ("-", 1, opAssoc.RIGHT, bar),
    ("^", 2, opAssoc.RIGHT, foo),
    ("*", 2, opAssoc.LEFT, foo),
    ("/", 2, opAssoc.LEFT, foo),
    ("+", 2, opAssoc.LEFT, foo),
    ("-", 2, opAssoc.LEFT, foo),
])

p = exp.parseString("-(10 + 20) * 30 / 4 ^ 1 + -2")
print(p)
print(p[0])
