from pyparsing import *
exp = Forward()
exp << ("a" ^ "a" + exp)
