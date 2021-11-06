from pyparsing import *
import operator

# TODO
# - control flow
# - functions
# - lists/dicts

# speed
ParserElement.enablePackrat()

# global/local environment -> make a class?
global_env = dict()
local_env = dict()

# model
class Prog():
    def __init__(self, exps):
        self.exps = exps

    def __str__(self):
        return "\n".join(map(lambda exp: str(exp[0]), self.exps))

    @classmethod
    def fromParseAction(cls, s, loc, toks):
        return cls(toks)

    def eval(self):
        return [exp[0].eval() for exp in self.exps][-1]

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

class Identifier(Exp):
    def eval(self):
        return global_env[self.exp]

class Asgn(Exp):
    def __init__(self, var, val):
        self.var = var
        self.val = val

    def __str__(self):
        return str(self.var) + " = " + str(self.val)

    def eval(self):
        global_env[self.var.exp] = self.val.eval()
        return global_env[self.var.exp]

class WhileLoop(Exp):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

    def __str__(self):
        return "while " + str(self.cond) + " {\n" + indent(str(self.body)) + "\n}"

    @classmethod
    def fromParseAction(cls, s, loc, toks):
        return cls(toks[1], toks[3])

    def eval(self):
        while self.cond.eval():
            ret = self.body.eval()
        return 0

def indent(str_prog, tab="  ", newline="\n"):
    ind = newline + tab
    return tab + ind.join(str_prog.split(newline))

# Parser
prog = Forward()

num = pyparsing_common.number
identifier = pyparsing_common.identifier
arith = infixNotation(num | identifier, [
    ("-", 1, opAssoc.RIGHT, UnOp.fromParseAction),
    ("^", 2, opAssoc.RIGHT, BinOp.fromParseAction),
    ("*", 2, opAssoc.LEFT, BinOp.fromParseAction),
    ("/", 2, opAssoc.LEFT, BinOp.fromParseAction),
    ("+", 2, opAssoc.LEFT, BinOp.fromParseAction),
    ("-", 2, opAssoc.LEFT, BinOp.fromParseAction),
])
asgn = identifier + Suppress("=") + arith
whileloop = "while" + arith + "{" + prog + "}"
exp = whileloop | asgn | arith
prog <<= ZeroOrMore(Group(exp))

num.setParseAction(Num.fromParseAction)
identifier.setParseAction(Identifier.fromParseAction)
asgn.setParseAction(Asgn.fromParseAction)
whileloop.setParseAction(WhileLoop.fromParseAction)
exp.setParseAction(Exp.fromParseAction)
prog.setParseAction(Prog.fromParseAction)

if __name__ == "__main__":
    p = prog.parseString("""
a = 1
b = 1
kaas = 10
while kaas {
  t = a
  a = b
  b = t + b
  kaas = kaas - 1
}
a
""")
    print('"""')
    print(p[0])
    print('"""')
    print(p[0].eval())
