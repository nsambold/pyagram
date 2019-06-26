#  firstpyagram.py TODOs:

## 1. frames and variables

organize all variables by frame (`framedict = {} #keys are frame count`)

- maybe create new id to each specific frame which 

- the built in id funtion returns the same id for different frames of the same function call

- need to add in the return value for frames # done

  

##2. functions and representation

be able to store the parents of functions.

- either from the function object itself(`func.parent() #returns parent`) or by storing when it was created(`funcdict[func] = parent`)
- maybe a seperate method for printing functions could be invoked within the print frames method when it comes across a function(this printFunction method could also be used to keep track of lambdas!)
- need to be able to represent user defined and built in functions differnetly
  - ex: def f() is different than f = print
- 



## 3. Objects and representation

need to be able to represent the class atributes and variables of user defined objects



inspect.getmembers(Dog)[2] will return the \_\_dict\_\_ of the Dog class which holds information like class variables and other stuff





## 3. knowing when to display/discard past frames

In the case where a function is called and none of the variables in that frame are needed outside the frame we need to know do discard/not display that frame



## 3. global/nonlocal keywords

be able to distinguish between global(nonlocal) or regular variables

<ul>
  <li> could check if the variable in the current and parent frame change at the same time</li>
</ul>

## 4. lambdas

1. be able to distinguish between multiple lambdas

   + ask Sequioa if he has a solution or look at python tutor for their solution









# Short-term

Current task: Add basic support for flags and frames. (See `Features.md`/"Bare bones".)

Game plan: (1) Get code from the student. (2) Modify it somehow. (3) Debug the modified code with `bdb` (i.e. PythonTutor). (4) Turn the result into a pyagram.

1. Figure out _what_ you want to do for steps (2) and (4) in the game plan above.

   * Some ideas:
     * `f(...)` $\to$ `nop(f(...))`
     * `f(...)` $\to$ `nop(helper(f, str(...)), f(...))`
     * `f(...)` $\to$ `nop(f)(x)`

2. Get familiar with the `bdb` (note: _not_ `pdb`), `inspect`, and `ast` modules.

3. Figure out _how_ to do step (2) in the game plan above.

   * If you can use `bdb` for debugging an AST, rather than debugging code, you could possibly (1) turn the code into an AST, (2) mutate it however you want, and then (3) debug it with `bdb`.

   * I haven't read [this](http://farmdev.com/src/secrets/framehack/index.html) but it looks cool.

   * Perhaps make an AST of the source code and then traverse it with a `Tracer` object that subclasses `NodeVisitor`? You could have said `Tracer` maintain dictionaries that represent the key-binding mappings for each frame.

     * Pro: This would make it easy to create flags and frames. In `visit_Call`, simply make a flag banner before you recursively traverse the children, and create a frame when you finish recursing on the children. (Note that for a program like `f(g(x))`, the `Call` node for `g` is actually very conveniently a child of the `Call` node for `f`.)
     * Con: Ideally we wouldn't have to explicitly maintain each frame, and we Python could do that for us.

     Complications:

     * I'm not exactly sure what happens when you come across a function call in the AST. At a preliminary glance, it seemed like the AST only cares to represent the global frame, and yet the following example proves that it does visit the internals of each function call:

       ```
       >>> import ast
       >>> src = """
       ... def f(x):
       ...     x += 1
       ...     y = x ** 2
       ...     return x + y
       ...
       ... z = f(4)
       ... """
       >>> tree = ast.parse(src)
       >>> class T(ast.NodeVisitor):
       ...     def visit_Pow(self, node):
       ...         print('yeet')
       ...         self.generic_visit(node)
       ...
       >>> T().visit(tree)
       yeet
       ```

     * I don't think ASTs can detect errors. Maybe you can execute one line of the AST at a time?

     * It's impossible to translate back from an AST into source code that you can debug.

4. Figure out _how_ to do step (4) in the game plan above.

# Long-term

Don't worry about this for now. Broadly speaking, we'll (1) write some code, (2) eventually migrate to GitHub, (3) add bells and whistles, and then (4) plan logistics for our research paper.

