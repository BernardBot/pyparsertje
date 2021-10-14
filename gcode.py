# https://en.wikipedia.org/wiki/G-code
# https://reprap.org/wiki/G-code

from pyparsing import *

letter = Char(alphas)
integer = pyparsing_common.integer
number = pyparsing_common.number

command = (letter + Optional(integer))("command")
params = dictOf(letter, Optional(number))("params")
checksum = ("*" + integer)("checksum")
comment = Regex(";.*")("comment")

gcode = command + Optional(params) + Optional(checksum) + Optional(comment)
