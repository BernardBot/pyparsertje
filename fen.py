from pyparsing import *

piece = oneOf("P N K B R Q p n k b r q")
rank = oneOf("1 2 3 4 5 6 7 8")
fyle = oneOf("a b c d e f g h")
square = fyle + rank
char = piece | rank
line = char*(1, 8)
number = Word(nums)

placement = (line + "/")*7 + line
color = oneOf("w b")
castle = "-" | oneOf("K Q k q")*(0, 4)
ep = "-" | square
half = number
full = number

fen = placement + color + castle + ep + half + full
