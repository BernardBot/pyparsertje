from pyparsing import *

class Asgn():
    def __init__(self, var, op, expr):
        self.var = var
        self.op = op
        self.expr = expr

    @classmethod
    def from_parse_action(cls, s, loc, toks):
        print(s, loc, toks)
        return cls(*toks)

var = Word(alphas)
expr = Word(nums)
asgn = var + "=" + expr

asgn.setParseAction(Asgn.from_parse_action)

result = asgn.parseString("kaas = 42")
print(result[0])
