
def f():
    def g(a):
        b = lambda : a
        return b
    q = g(1)
    w = g(2)
f()
