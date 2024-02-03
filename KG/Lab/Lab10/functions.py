from math import *

def f1(x, z):
    return x + z


def f2(x, z):
    return sin(x + z ** 2)


def f3(x, z):
    return exp(cos(x) * sin(z))


def f4(x, z):
    return cos(x + z)

CHOICE = [
    "x + z",
    "sin(x + z ** 2)",
    "exp(cos(x) * sin(z))",
    "cos(x + z)"
]