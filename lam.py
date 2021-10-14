from pyparsing import *
exp = Forward()
var = pyparsing_common.identifier
app = exp*(1,)
lam = "\\" + var*(1,) + "->" + exp
exp <<= lam | "(" + exp + ")" | app
