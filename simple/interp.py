from parse import simple
import examples
import operator
from pyparsing import ParseResults

def run(str):
    return interp(simple.parseString(str))

# if we have variables we need to somehow add
# an environment
def interp(prog):
    for expr in prog:
        print(expr, "=", interp_expr(expr))

def interp_expr(expr):
    # here we need pattern matching
    # it works now, because our language is so easy
    # we only have binary operators or numbers
    if type(expr) == ParseResults:
        e1, op, e2 = expr
        v1 = interp_expr(e1)
        fn = ops[op]
        v2 = interp_expr(e2)
        return fn(v1, v2)
    return expr

ops = {
    "*" : operator.mul,
    "/" : operator.truediv,
    "+" : operator.add,
    "-" : operator.sub,
}

if __name__ == "__main__":
    run(examples.p0)
