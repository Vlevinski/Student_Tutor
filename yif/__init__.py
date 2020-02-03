#!python3.7
#
import random


def get_wordlist(x):
    return ('foo' if (x == 1) else
            'bar' if (x == 2) else
            'baz' if (x == 3) else
            'qux' if (x == 4) else
            'quux')


print([get_wordlist(random.randint(1, 4)) for item in range(10)])
