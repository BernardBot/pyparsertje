from pyparsing import *

class Var():
    def __init__(self, name):
        self.name = name

    @classmethod
    def foo():
        pass

class Asgn():
    def __init__(self, var, op, expr):
        self.var = var
        self.op = op
        self.expr = expr

word = Word(alphas)
asgn = word + "=" + word

word.setParseAction(lambda loc, s, toks: print(loc))
asgn.setParseAction(lambda toks: Asgn(*toks.asList()))

result = asgn.parseString("x = kaas")
print(result)
