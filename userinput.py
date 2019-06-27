
class C():
    def __repr__(self):
        x = 1
        def f():
            x = 2
            return x
        a = f()
        return "hi"
c = C()
print(c)
