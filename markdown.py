from pyparsing import *

word = Word(alphas + alphas.upper())
text = OneOrMore(word)
integer = Word(nums)
hichar = oneOf("* _")
hightlight = hichar[1,3] + text + hichar[1,3]
heading = Char("#")[1,6] + text
blockquote = ">" + text
olist = OneOrMore(integer + "." + text)
ulchar = oneOf("* _ - +")
ulist = OneOrMore(ulchar + text)
lyst = olist | ulist
code = "`" + text + "`"
rules = "***" | "---" | Char("_")[3,]
link = "[" + text + "]" + "(" + text + Optional('"' + text + '"') + ")"
url = "<" + text + ">"
image = "![" + text + "!]" + "(" + text + Optional('"' + text + '"') + ")"
