def f(x, g):
    return g(x) + 10

def kuadrat(x):
    return x ** 2

def kubik(x):
    return x ** 3

print f(3, kuadrat)
print f(3, kubik)
print f(3, lambda x: x ** 4)