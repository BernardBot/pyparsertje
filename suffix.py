from pyparsing import *
from pydantic import BaseModel
from typing import List, Any

class Suffix(BaseModel):
    mem_no : int = 0
    motor_id : int = 1
    sign : str = None

class Code(BaseModel):
    symbol : str
    suffix : Suffix

class Prog(BaseModel):
    codes : List[Code]

integer = pyparsing_common.integer
symbol = oneOf("V P")
sign = oneOf("+ -")
suffix = (
    Optional(integer)("mem_no") +
    Optional("." + integer("motor_id")) +
    Optional(sign)("sign")
).setParseAction(Suffix.parse_obj)
code = (symbol("symbol") + suffix("suffix")).setParseAction(Code.parse_obj)
# ugh the struggle with lists is annoying
prog = ZeroOrMore(code).setParseAction(lambda toks: Prog(codes=list(toks)))

suffix.runTests("""
        1.1+
        .1+
        1+
        1
        +
        -
        .1
""")
prog.runTests(["""
    V1.1+
    P1
    V+
"""])

p = prog.parseString("""
    V1.1+
    P1
    V+
""")[0]

