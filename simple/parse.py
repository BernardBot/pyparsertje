from pyparsing import *

# idiom for significant speed up
ParserElement.enablePackrat()

number = pyparsing_common.number
atom = number

arith = infixNotation(atom, [
    ("*", 2, opAssoc.LEFT),
    ("/", 2, opAssoc.LEFT),
    ("+", 2, opAssoc.LEFT),
    ("-", 2, opAssoc.LEFT),
])

simple = ZeroOrMore(arith)
