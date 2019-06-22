import bdb
import pdb
import os
import firstpyagram
import test


# bp = bdb.Breakpoint(os.path.realpath(__file__), 20)
# bp.bpprint()

def f(x, h = None):
    return x
def g(y):
    return y + 1
def h(q):
    return q - 1

t = bdb.Tdb()
t.run('f(g(2), h(3)); f(h(g(2)))', globals())
print()
fi = firstpyagram.stringtofile(test.test1)
s = fi.read()

t.run(test.test1)
print()
t.run('f(g(2), h(3)); f(h(g(2)))', globals())





f(g(2), h(3))
f(h(g(2)))
