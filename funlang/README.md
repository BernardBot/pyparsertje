you can add parseActions to infixNotation tuples
left-associative operators can return longer lists
  e.g.: 10 + 20 + 30 -> [[10, '+', 20, '+', 30]]
operators are wrapped and in parseActions we need to do toks[0]
  e.g.: setParseAction(lamdba toks: `MyClass(*(toks[0]))`

