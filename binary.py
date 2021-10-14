from pyparsing import *
exp = Forward()
exp <<= "0" + exp | "1" + exp | Empty()
regexp = Regex("[01]*")
