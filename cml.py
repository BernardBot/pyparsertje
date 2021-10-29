from pyparsing import *

ParserElement.enablePackrat()

cml = Forward()

integer = pyparsing_common.integer
suffix = Optional(integer) + Optional("." + integer)
code = oneOf("| |1 |2 ^ [ $ ) (1 ( O F ] ]1 # } * *1 > < [L ]L ? S A P M Y Q Z C J I O F T W V CL JL I T W V") + suffix
circ = "@" + suffix + oneOf("+ -")
area = "\\" + oneOf("P N") + integer
atom = code | circ | area | integer

arith = infixNotation(atom, [
    ("U1", 1, opAssoc.RIGHT),
    ("U2", 1, opAssoc.RIGHT),
    ("U3", 1, opAssoc.RIGHT),
    ("*", 2, opAssoc.LEFT),
    ("/", 2, opAssoc.LEFT),
    ("+", 2, opAssoc.LEFT),
    ("-", 2, opAssoc.LEFT),
    ("=", 2, opAssoc.RIGHT),
])
logic = infixNotation(atom, [
    ("!!", 1, opAssoc.RIGHT),
    ("==", 2, opAssoc.LEFT),
    ("!=", 2, opAssoc.LEFT),
    ("<=", 2, opAssoc.LEFT),
    (">=", 2, opAssoc.LEFT),
    (">", 2, opAssoc.LEFT),
    (">", 2, opAssoc.LEFT),
    ("&&", 2, opAssoc.RIGHT),
    ("||", 2, opAssoc.RIGHT),
])

asgn = atom + oneOf("= += -=") + arith
concat = delimitedList(arith, oneOf(", ;"))
branch = logic + "," + delimitedList(arith, ":") + "," + delimitedList(arith, ":")
loop = "X" + suffix + cml + "X" + suffix + "-"
bank = "B" + suffix + cml + "END"
ladr = "L" + suffix + cml + "END"
comment = dblSlashComment

statement = asgn | branch | loop | bank | ladr | atom | concat | comment
cml <<= ZeroOrMore(Group(statement))
