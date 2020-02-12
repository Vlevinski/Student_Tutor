#!pythone3.7
#

import random

def r_init(a=None):
    # init internal state
    return random.seed(a)

def r_state():
    # get internal state object
    return random.getstate()

def r_int(a=None, b=None):
    # get random int in not mandatory range a,b
    if not a or not b: a=0; b=1
    return random.randint(a,b)

def r_range(a,b):
    # get random int in mandatory arguments range a,b
    return random.randint(a,b)

