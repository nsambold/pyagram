import bdb
import pdb
import inspect
import sys
import ast


node = ast.parse('')





# bdb.test()





# def lambdaHelper(x):
#     id = x
#
#
# x = lambda x, y = lambdaHelper(1): lambda y, , x = lambdaHelper(1): x + y
# x(1)(2)
def f(x, h = None):
    return x

def g(y):
    return y + 1

def h(q):
    return q - 1

#
pdb.run("f(h(g(2)))")
# pdb.run("f(g(2), h(3))")
# debug = bdb.Bdb()

# print(debug.run("f(g(2), h(3))", globals()))
# debug.run(globals(), "f(h(g(2)))")
f(g(2), h(3))

f(h(g(2)))

# q = 1 / 0



#
#
# def nop(f):
#     return f
#
# nop(f(nop(g(2))))
#
# nop   (g(2))
# nop(f(3))








# def createFlag(func):
#     print(func)
#
# def f(x):
#     return x + 2
#
# oldf = f
# def newf(param):
#     createFlag(f)
#     return f(param)
#
# f = newf
#
# f(2)
#
# def g(x):
#     return x + 1
#
# def newg(param):
#     createFlag(g)
#     return g(param)
#
# g = newg
