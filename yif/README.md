# Advanced conditional expresions, functions

## *multi-line if:*

if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
elif <expr>: <statement_1>; <statement_2>; ...; <statement_n>
else <expr>: <statement_1>; <statement_2>; ...; <statement_n>
<statement_1>; <statement_2>; ...; <statement_n>

## *one-line expresion:*

<expr1> if <conditional_expr> else <expr2>
print("Let's go to the", 'beach' if not raining else 'library')

*a = 'yes' if ('qux' in list('foo', 'bar', 'baz')) else 'no'*
*z = 1 + (x if x > y else y) + 2*

*x = random.randint(1,4)
s = ('foo' if (x == 1) else
     'bar' if (x == 2) else
     'baz' if (x == 3) else
     'qux' if (x == 4) else
     'quux'
)*
