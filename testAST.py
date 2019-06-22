import ast
import bdb

import test

ASTnode = ast.parse("""
def f(x, h = None):
    a = 1
    return x
def g(y):
    b = 2
    return y + 1
def h(q):
    return q - 1
f(g(3))
""")
code = compile(ASTnode, filename = "<ast>", mode = "exec")

class Tdb(bdb.Bdb):
    def user_call(self, frame, args):
        # print('locals:', frame.f_locals)
        # print('\nframe info:', inspect.getframeinfo(frame))
        name = frame.f_code.co_name
        if not name: name = '???'
        print('+++ call', name, args)
    def user_line(self, frame):
        import linecache
        name = frame.f_code.co_name
        if not name: name = '???'
        fn = self.canonic(frame.f_code.co_filename)
        line = linecache.getline(fn, frame.f_lineno, frame.f_globals)
        print('+++', fn, frame.f_lineno, name, ':', line.strip())
    def user_return(self, frame, retval):
        print('+++ return', retval)
    def user_exception(self, frame, exc_stuff):
        print('+++ exception', exc_stuff)
        self.set_continue()


t = bdb.Tdb() # make our own version of the Tdb class
t.run(code) # don't need to use globals()
