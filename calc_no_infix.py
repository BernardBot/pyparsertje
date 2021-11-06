from pyparsing import *

calc = Forward()
exp2 = Forward()
exp1 = Forward()
exp0 = Forward()

number = pyparsing_common.number
atom = number | Group("(" + calc + ")")

exp2 <<= atom + Optional("^" + atom)
exp1 <<= exp2 + Optional("*" + exp2)
exp0 <<= exp1 + Optional("+" + exp1)
calc <<= exp0
