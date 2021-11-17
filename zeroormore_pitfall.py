from pyparsing import *

word = Word(alphas)("word")
exp = ZeroOrMore(word)
