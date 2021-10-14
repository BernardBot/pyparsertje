from pyparsing import *

calc = infixNotation(
        pyparsing_common.number,
        [
            ("+", 2, opAssoc.LEFT)
        ]
)
