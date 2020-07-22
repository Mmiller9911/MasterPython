# Namespaces : A namespace is a ''container'' where names are mapped to objects, they are used to avoid confusions in cases where same names exist in different namespaces. They are created by modules, functions, classes.
#
# Scope : A scope defines the hierarchical order in which the namespaces have to be ''searched'' in order to obtain the mappings of name-to-object(variables). It is a context in which variables exist and from which they are referenced. It defines the accessibility and the lifetime of a variable.
#
#
# Scope resolution via LEGB rule :
# In Python, the LEGB rule is used to decide the order in which the namespaces are to be searched for scope resolution.
# The scopes are listed below in terms of hierarchy(highest to lowest/narrowest to broadest):
#
# Local(L): Defined inside function/class
# Enclosed(E): Defined inside enclosing functions(Nested function concept)
# Global(G): Defined at the uppermost level
# Built-in(B): Reserved names in Python builtin modules


def spam1():


    def spam2():


        def spam3():
            z = ' 3 '
            z += y
            print('in spam3 locals are {}'.format(locals()))
            print('spam3 can check itself and spam 1 + spam 2 which enclose it')
            return z

        y = ' 2 ' + x
        y += spam3()
        print('in spam2 locals are {}'.format(locals()))
        print('spam2 can check itself and spam 1 which enclose it')
        return y

    x = ' 1 '
    x+= spam2()
    print('in spam1 locals are {}'.format(locals()))
    print('spam1 can check itself')
    # print(y)
    # print(z)
    return x

print(spam1())
