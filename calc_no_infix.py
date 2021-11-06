from pyparsing import *

calc = Forward()
exp2 = Forward()
exp1 = Forward()
exp0 = Forward()

number = pyparsing_common.number
atom = number | Group("(" + calc + ")")

exp2 <<= atom + ZeroOrMore("^" + exp2)
exp1 <<= exp2 + ZeroOrMore("*" + exp2)
exp0 <<= exp1 + ZeroOrMore("+" + exp1)
calc <<= exp0

p = calc.parseString("1+2+3*3")
print(p)
