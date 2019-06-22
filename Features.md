# Back-end

## Bare bones: flags and frames

* Add basic support for flags and frames.
* Add basic support for `lambda` functions.
* Add basic support for user-defined objects.
* Address existing bugs in PythonTutor:
  * Fix the frame-id bug in pg_logger. (See Fall 2017, MT2 Q2.)
  * Make sure `__str__` and `__repr__` are executed when appropriate. (Right now, PythonTutor doesn't go into `__repr__` if you call `print` without a `__str__` function.)

## Add-ons

* `lambda` functions should have subscripts (as in your textbook), so people can tell them apart easily.
  * When you come across a `lambda` function, perhaps you can somehow turn it into a non-anonymous function. (For instance, maybe you can wrap it in a unique no-op which gives it an identity? Or change its `.__name__` attribute, if it has one?)
  * You might be able to do this by walking the AST and transforming the `lambda` nodes. (Every AST node has not only a `lineno` but also a `col_offset`, which may be handy.)
* Objects should be rendered as in the "OOP" chapter of your textbook.
  * Consider how to render bound methods. (This'll take some experimenting in the interpreter too, to figure out how Python handles bound methods.)
* Iterators should be rendered as in the "Iterators & Generators" chapter of your textbook.
* Generators should be rendered as in the "Iterators & Generators" chapter of your textbook, but with a slight modification. Each generator object should get its own frame (similar to the way that you render instances for OOP diagrams), to keep track of the local variables specific to that generator instance.
* `<listcomp>`, `<dictcomp>`, `<setcomp>`, etc. should either be rendered well, or not rendered at all. (For example, see how PythonTutor does `[str(x) for x in range(4)]`. It's horrible. ".0" gets bound to the iterator object and the return values of the `str(x)` don't appear until the very end!)
  * These correspond to `ListComp`,  `SetComp`, `GeneratorExp`, `DictComp`, and `comprehension` nodes in the AST.
* If you see `f(*args)`, the flag should show `args` being bound to a tuple of all the provided arguments.
  * This corresponds to a `Starred` node in the AST.
* Handle `import` statements.
  * See how PythonTutor does it. Only a few modules are "legal".
  * `import` statements correspond to the `Import`, `ImportFrom`, and `alias` nodes in the AST.
* Add support for f-strings.

# Front-end

* The code should be on the left, and the diagram on the right.
  * At the bottom of the right panel there should be a `Print Output` box, so as to support print statements. (Perhaps you can find a way to let people adjust its height to be taller or shorter, too.)
  * At the bottom of the left panel there should a few options that change the way the diagram gets rendered.
    * [Default ON] Draw values / arrows under each operand / operator in the flag.
    * [Default ON] Draw fancy linked lists, trees, and graphs.
      * Release a pip module called `pyagram`, so people can write `import pyagram as pg`. It should just include simple `Link`, `Tree`, and `Graph` classes.
        * People should be able to view their implementations somewhere, perhaps inside your textbook.
        * For the `pyagram.Graph` implementation, you should have a main `Graph` class whose `__init__` method merely defers to either its `UndirectedGraph` subclass or its `DirectedGraph` subclass, depending on whether the user has supplied edge weights.
      * Then, when people instantiate a `pyagram.Link` (and the option is ON), said `pyagram.Link` will get rendered as in CS 61A (box-and-pointer style) rather than the manner in which you typically render user-defined objects / instances in Pyagram. The same principle goes for instances of `pyagram.Tree`. For `pyagram.Graph` instances you can make up your own fancy visualization, as there's no precedent in CS 61A — for instance, you could render a `pyagram.Graph` as a pointer to a big box, in which you can see all the graph's vertices and edges with labels.
    * [Default OFF] Go into `__str__` and `__repr__` methods.
      * Off by default, because it'd otherwise be super annoying every time you call `print`. But it's important that CS 61A students can visualize `__str__` and `__repr__` when they get to OOP.
* When you modify the code (or change any of the options on the left panel), the diagram should get a semi-opaque overlay to indicate it's out of date.
* Make everything aesthetically pleasing.
  * Display `lambda` functions as `λ` instead of `<lambda>`.
  * Some things are not labeled well. For instance, why label a frame "frame 1: f"? It doesn't correspond to the function f; it corresponds to the function call f(5). So how about "frame 1: f(5)"? (Or maybe just "frame 1" if that's too repetitive, given that the flag already communicates that?)
  * Etc.
* Consider colour coding (to distinguish between primitives, lists, instances, frames, etc.).
* Shareable links. (This is important for people to be able to send them to friends or post them on Piazza.) The URL can either contain the code the user wrote, its Burrows-Wheeler transform, or the serialization of the diagram itself.
* Embeddable links, or some way to download a sequence of SVGs that correspond to the diagram. (This is important so you can use them in your textbook.)