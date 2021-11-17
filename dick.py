from pyparsing import *

key = Word(alphas)
value = Word(alphas)
member = Group(key + Suppress(":") + value)
members = delimitedList(member)
dick = Dict(Suppress("{") + Optional(members) + Suppress("}"))
