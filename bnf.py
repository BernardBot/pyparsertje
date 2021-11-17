# https://github.com/pyparsing/pyparsing/blob/0ef76494861cd1d4a69a11e8df95c804e63a4369/examples/fourFn.py#L47
e = CaselessKeyword("E")
pi = CaselessKeyword("PI")
fnumber = Regex(r"[+-]?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?")
ident = Word(alphas, alphanums + "_$")

plus, minus, mult, div = map(Literal, "+-*/")
lpar, rpar = map(Suppress, "()")
addop = plus | minus
multop = mult | div
expop = Literal("^")

expr = Forward()
expr_list = delimitedList(Group(expr))

fn_call = (ident + lpar - Group(expr_list) + rpar).setParseAction(
    insert_fn_argcount_tuple
)
atom = (
    addop[...]
    + (
        (fn_call | pi | e | fnumber | ident).setParseAction(push_first)
        | Group(lpar + expr + rpar)
    )
).setParseAction(push_unary_minus)

# by defining exponentiation as "atom [ ^ factor ]..." instead of "atom [ ^ atom ]...", we get right-to-left
# exponents, instead of left-to-right that is, 2^3^2 = 2^(3^2), not (2^3)^2.
factor = Forward()
factor <<= atom + (expop + factor).setParseAction(push_first)[...]
term = factor + (multop + factor).setParseAction(push_first)[...]
expr <<= term + (addop + term).setParseAction(push_first)[...]
bnf = expr
