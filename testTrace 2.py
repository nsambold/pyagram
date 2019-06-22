import bdb
import pdb
import inspect


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

debug = bdb.Bdb
# print(inspect.signature(debug.run))
debug.run("f(g(2), h(3))", "f(g(2), h(3))")
debug.run("f(h(g(2)))", "f(h(g(2)))")
# debug.run(bdb.Bdb, f(g(2), h(3)))
#
# debug.run(bdb.Bdb, f(h(g(2))))



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
