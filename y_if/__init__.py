#!python3.7
#
import random


def get_wordlist(x):
    return ('foo' if (x == 1) else
            'bar' if (x == 2) else
            'baz' if (x == 3) else
            'qux' if (x == 4) else
            'quux')


def get_index(words, el):
    return words.index(el)


def get_word(words,idx):
    return words[idx]

'''
print([get_wordlist(random.randint(1, 4)) for item in range(10)])
print (get_index(['bar', 'foo', 'baz', 'qux', 'quux'],'qux'))
print (get_word(['bar', 'foo', 'baz', 'qux', 'quux'],3))
'''
