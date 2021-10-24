from pyparsing import *

COLON, LSB, RSB, LCB, RCB = map(Suppress, ":[]{}")

objekt = Forward()
array = Forward()

number = pyparsing_common.number
string = QuotedString('"')
value = number | string | objekt | array | "true" | "false" | "null"
member = string + COLON + value
members = Optional(delimitedList(Group(member)))
objekt <<= Dict(LCB + members + RCB)
array <<= LSB + Optional(delimitedList(value)) + RSB

json = value
