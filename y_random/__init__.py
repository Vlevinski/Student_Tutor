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
    if not a or not b:
        a, b = 0, 1
    return random.randint(a, b)


def r_range(a, b):
    # get random int in mandatory arguments range a,b
    return random.randint(a, b)


def r_random():
    # get float in range 0.0 1.0
    return random.random()


def r_number(a, b):
    # return float number in range a,b:
    return random.uniform(a, b)


def r_one():
    s = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
    return random.choice(s)


def r_rname():
    s = ["Nick", "Peter", "John", "Nick", "Andrew", "Paul", "Cris", "David", "Robert", "Richard", "Mark"]
    return random.choice(s)


def r_sname():
    s = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    return random.choice(s)
