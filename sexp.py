from pyparsing import *
sexp = Forward()
atom = pyparsing_common.identifier
lyst = "(" + sexp*(0,) + ")"
sexp <<= lyst | atom
