from pyparsing import *

number = pyparsing_common.number
com = infixNotation(
        number + "j" | number,
        [
            ("-", 1, opAssoc.RIGHT),
            ("+", 2, opAssoc.LEFT),
            ("-", 2, opAssoc.LEFT),
        ]
)
