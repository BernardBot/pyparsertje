from pyparsing import *

number = pyparsing_common.number

calc = Forward()

real = number
imag = number + "j"
func = Word(alphas) + "(" + calc + ")"
cons = Word(alphas)

calc <<= infixNotation(
        func | cons | imag | real,
        [
            ("-", 1, opAssoc.RIGHT),
            ("+", 1, opAssoc.RIGHT),
            ("^", 2, opAssoc.RIGHT),
            ("/", 2, opAssoc.LEFT),
            ("*", 2, opAssoc.LEFT),
            ("+", 2, opAssoc.LEFT),
            ("-", 2, opAssoc.LEFT),
        ],
)
