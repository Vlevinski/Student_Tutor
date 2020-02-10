#!python3.7
#
# import random


def get_one(x):
    """
    # return the word related to value x in range 1-5
    :param x:
    :return:
    """
    return ('foo' if (x == 1) else
            'bar' if (x == 2) else
            'baz' if (x == 3) else
            'qux' if (x == 4) else
            'quux')


def get_index(words, el):
    """
    # get index of the word in the words list
    :param words:
    :param el:
    :return:
    """
    return words.index(el)


def get_word(words, idx):
    """
    # return the word with index idx
    :param words:
    :param idx:
    :return:
    """
    return words[idx]


'''
print([get_wordlist(random.randint(1, 4)) for item in range(10)])
print (get_index(['bar', 'foo', 'baz', 'qux', 'quux'],'qux'))
print (get_word(['bar', 'foo', 'baz', 'qux', 'quux'],3))
'''
