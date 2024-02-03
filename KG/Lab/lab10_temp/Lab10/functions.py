from math import *

def f1(x, z):
    return x + z


def f2(x, z):
    return cos(x) * sin(z)


def f3(x, z):
    return exp(cos(x) * sin(z))


def f4(x, z):
    return cos(x) * z / 3

CHOICE = [
    "x + z",
    "cos(x) * sin(z)",
    "exp(cos(x) * sin(z))",
    "cos(x) * z / 3"
]