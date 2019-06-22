test1 = """
def f(x, h = None):
    a = 1
    return x
def g(y):
    b = 2
    return y + 1
def h(q):
    return q - 1
f(g(2), h(3)); f(h(g(2)))
"""
testframe = """
a = 1
def f():
    a = 3
    b = 2
    return b
c = f()
"""

import linecache
print(linecache.getline(__file__, 2))

test2 = """
def f():
    a = 1
    b = 2
    c = "3"
    d = lambda x: x
    print(globals())
    e = f
    f = print("hi")
    g = [1, d, 3]
    print(locals())

f()
"""


test3 = """
x=locals()
def g(y):
    b = 2
    return y + 1
def h(q):
    return q - 1
g(h(7))
"""

#
