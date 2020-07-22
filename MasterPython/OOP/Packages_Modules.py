
# Fibonacci numbers module
# A module is a file containing Python definitions and statements.
# The file name is the module name with the suffix .py appended
# Within a module, the module’s name (as a string) is available as the value of the global variable __name__
# import fibo - This does not enter the names of the functions defined in fibo directly; it only enters the module name fibo there
# Using the module name you can access the functions
# Each module has its own private symbol table, which is used as the global symbol table by all functions defined in the module
# if you know what you are doing you can touch a module’s global variables with the same notation used to refer to its functions, modname.itemname.
# Modules can import other modules
# The imported module names are placed in the importing module’s global symbol table
# There is a variant of the import statement that imports names from a module directly into the importing module’s symbol table from fibo import fib, fib2
# print(dir()) displays the modules objects
# When a module named spam is imported, the interpreter first searches for a built-in module with that name.
# If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path

# Python comes with a library of standard modules, described in a separate document,
# the Python Library Reference (“Library Reference” hereafter).
# Some modules are built into the interpreter; these provide access to operations
# that are not part of the core of the language but are nevertheless built in, either for efficiency or to provide access
# to operating system primitives such as system calls

# from SeleniumFramework.pages.Checkout import CheckoutPage = from package folder.package folder.filename import class name

# if __name__ == "__main__": execute the module as a script
#     import sys
#     fib(int(sys.argv[1]))
import sys

import SeleniumBehave
from SeleniumFramework.pages.Checkout import CheckoutPage

# The built-in function dir() is used to find out which names a module defines. It returns a sorted list of strings
# Without arguments, dir() lists the names you have defined currently - Note that it lists all types of names: variables, modules, functions, etc.
print(dir(sys))    # returns ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print(dir(SeleniumBehave))
print(dir())
print(__builtins__)
print(__file__)
print(__doc__)
print(__name__)
print(__package__)
#print(__spec__)
#print(__annotations__)
#print(__cached__)
#print(__loader__)

print(globals())
# returns {'__name__': '__main__',
# '__doc__': None,
# '__package__': None,
# '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x011DAF58>,
# '__spec__': None,
# '__annotations__': {},
# '__builtins__': <module 'builtins' (built-in)>,
# '__file__': 'C:/Users/Matt/PycharmProjects/MasterPython/Packages_Modules.py',
# '__cached__': None
# 'SeleniumBehave': <module 'SeleniumBehave' from 'C:\\Users\\Matt\\PycharmProjects\\MasterPython\\SeleniumBehave\\__init__.py'}


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# When a module named spam is imported, the interpreter first searches for a built-in module with that name.
# If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path
sys.path.append('C:\\Users\\Matt\\PycharmProjects\\MasterPython\\SeleniumBehave\\CommonFuncs')
print(sys.path)  # A list of strings that specifies the search path for modules.
#  As initialized upon program startup, the first item of this list,
#  path[0], is the directory containing the script that was used to invoke the Python interpreter
# [C:\\Users\\Matt\\PycharmProjects\\MasterPython\\OOP',
# 'C:\\Users\\Matt\\PycharmProjects\\MasterPython',
# 'C:\\Python\\python38.zip',
# 'C:\\Python\\DLLs',
# 'C:\\Python\\lib',
# 'C:\\Python',
# 'C:\\Python\\lib\\site-packages']

# After initialization, Python programs can modify sys.path.
# The directory containing the script being run is placed at the beginning of the search path,
# ahead of the standard library path.
# I also learned that all packages are modules, (although not all modules are packages) so that is why my error was complaining about how the module didn't have the attribute.

# Packages are a way of structuring Python’s module namespace by using “dotted module names”.
# The __init__.py files are required to make Python treat directories containing the file as packages.
# In the simplest case, __init__.py can just be an empty file, but it can also execute initialization code for the package or set the __all__ variable, described later.


# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               mp3read.py
#               mp3write.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py       Initialize the effects package
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py       Initialize the filters package
#               equalizer.py
#               vocoder.py
#               karaoke.py

#  Users of the package can import individual modules from the package, for example:
#  import sound.effects.echo        #  This loads the submodule sound.effects.echo. It must be referenced with its full name. sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
#  OR
#  from sound.effects import echo  # This also loads the submodule echo, and makes it available without its package prefix, so it can be used as follows: echo.echofilter(input, output, delay=0.7, atten=4)
#  OR
#  from sound.effects.echo import echofilter # Again, this loads the submodule echo, but this makes its function echofilter() directly available - echofilter(input, output, delay=0.7, atten=4)

#  Note that when using from package import item, the item can be either a submodule (or subpackage) of the package, or some other name defined in the package, like a function, class or variable


# from sound.effects import *
# The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__,
# it is taken to be the list of module names that should be imported when from package import * is encountered.
# It is up to the package author to keep this list up-to-date when a new version of the package is released.
# Package authors may also decide not to support it, if they don’t see a use for importing * from their package.

# For example, the file sound/effects/__init__.py could contain the following code:
# __all__ = ["echo", "surround", "reverse"]
# This would mean that from sound.effects import * would import the three named submodules of the sound package.

# If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package
# sound.effects into the current namespace; it only ensures that the package sound.effects has been imported (possibly running any initialization code in __init__.py)
# and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by __init__.py.

# If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package sound.effects into the current namespace; it only ensures that the package sound.effects has been imported (possibly running any initialization code in __init__.py) and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by __init__.py. It also includes any submodules of the package that were explicitly loaded by previous import statements. Consider this code:
#
# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *
# In this example, the echo and surround modules are imported in the current namespace because they are defined in the sound.effects package when the from...import statement is executed. (This also works when __all__ is defined.)
#
# Although certain modules are designed to export only names that follow certain patterns when you use import *, it is still considered bad practice in production code.
#
# Remember, there is nothing wrong with using from package import specific_submodule! In fact, this is the recommended notation unless the importing module needs to use submodules with the same name from different packages.

# When packages are structured into subpackages (as with the sound package in the example),
# you can use absolute imports to refer to submodules of siblings packages.
# For example, if the module sound.filters.vocoder needs to use the echo module in the sound.effects package, it can use from sound.effects import echo

#  You can also write relative imports, with the from module import name form of import statement. These imports use leading dots to indicate the current and parent packages involved in the relative import. From the surround module for example, you might use:
#  from . import echo
#  from .. import formats
#  from ..filters import equalizer

# Packages in Multiple Directories
# Packages support one more special attribute, __path__. This is initialized to be a list containing the name of the directory holding the package’s __init__.py before the code in that file is executed. This variable can be modified; doing so affects future searches for modules and subpackages contained in the package.
# While this feature is not often needed, it can be used to extend the set of modules found in a package.

# https://readthedocs.org/projects/behave/downloads/pdf/latest/