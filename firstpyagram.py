first = dict.copy(globals())
import bdb, inspect, ast
import test

def stringtofile(str):
    f = open("input2.py", "w")
    f.write(str)
    f.close()
    f = open("input2.py", "r")
    return f

def linegetter(frame):
    import linecache
    fn = 'input2.py'
    line = linecache.getline(fn, frame.f_lineno, frame.f_globals)
    return line

class printvars(bdb.Bdb):
    def user_call(self, frame, args):
        print(globals())

    def user_line(self, frame):
        print(globals())

    def user_return(self, frame, value):
        print(globals())

    def user_exception(self, frame, exception):
        print(globals())

class pyagram(bdb.Bdb):
    # natural = {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x107b1d080>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'firstpyagram.py', '__cached__': None}
    glst = {}
    llst = {}

    def user_func(self, frame, third = None):
        # print(frame.f_locals)
        # print(frame.f_globals)
        import linecache
        line = linegetter(frame)
        astnode = ast.parse(test.test1)
        print("user_line: \n", line)

    # will return the last created variable
    def dicchange(self, curframe1234):
        if curframe1234.f_globals == curframe1234.f_locals: # we are in the global frame
            if not glst:
                glst = curframe1234.f_globals
            print(curframe1234.f_globals.items() - glst.items())
            glst = curframe1234.f_globals.items()
        else: # we are in some function call
            if not llst:
                llst = curframe1234.f_locals
            print(curframe1234.f_locals.items() - llst.items())


        # elif:
        #
        # else:
        #     var = frame.f_locals
        #     if var.items() - llst.items() == var.items():
        #         print(var.items() - glst.items())
        #     else:
        #         print(var.items() - llst.items())

    def user_call(self, frame, args):
        if frame.f_globals == frame.f_locals: # we are in the global frame
            if not glst:
                glst = frame.f_globals
            print(frame.f_globals.items() - glst.items())
            glst = frame.f_globals.items()
        else: # we are in some function call
            if not self.glst:
                self.glst = frame.f_locals
            out = frame.f_locals.items() - self.llst.items()
            print(out)
        # print("\n-------------------------", frame.f_globals['x'], "\n")
        self.user_func(self, frame, args)
        # print(frame.f_locals)
        # print(frame.f_globals)
        # import linecache
        # line = linegetter(frame)
        # astnode = ast.parse(test.test1)
        # # print(fn, frame.f_lineno, frame.f_globals)
        # print("user_call: \n", line)

        # print('locals:', frame.f_locals)
        # print('\nframe info:', inspect.getframeinfo(frame))

        #print('\narg spec:', inspect.formatargspec(*inspect.getfullargspec(f)))
        # don't have a function to call formateargspec on

    def user_line(self, frame):
        if frame.f_globals == frame.f_locals: # we are in the global frame
            if not self.glst:
                self.glst = frame.f_globals
            out = frame.f_globals.keys() - self.glst.keys()
            print(out)
            self.glst = frame.f_globals.items()
        else: # we are in some function call
            if not self.llst:
                self.llst = frame.f_locals
            out = frame.f_locals.items() - self.llst.items()
            print(out)
        # print("\n-----------------", frame.f_globals, "\n\n")
        self.user_func(self, frame)

    def user_return(self, frame, value):
        if frame.f_globals == frame.f_locals: # we are in the global frame
            if not self.glst:
                self.glst = frame.f_globals
            print(frame.f_globals.items() - self.glst.items())
            self.glst = frame.f_globals.items()
        else: # we are in some function call
            if not self.glst:
                self.glst = frame.f_locals
            out = frame.f_locals.items() - self.llst.items()
            print(out)
        self.user_func(self, frame)

    def user_exception(self, frame, exception):
        if frame.f_globals == frame.f_locals: # we are in the global frame
            if not self.glst:
                self.glst = frame.f_globals
            print(frame.f_globals.items() - self.glst.items())
            self.glst = frame.f_globals.items()
        else: # we are in some function call
            if not self.glst:
                self.glst = frame.f_locals
            out = frame.f_locals.items() - self.llst.items()
            print(out)
        self.user_func(self, frame)

# print(first)

t = pyagram()
inputfile = stringtofile(test.test3)
string = inputfile.read()
t.run(string, first)




"""
#Tdb example class from bdb.py
class Tdb(Bdb):
    def user_call(self, frame, args):
        name = frame.f_code.co_name
        if not name: name = '???'
        print('+++ call', name, args, sys.__dict__)
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
"""









#
