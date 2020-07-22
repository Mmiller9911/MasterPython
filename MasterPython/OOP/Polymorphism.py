# Polymorphism is the ability of an object to take on many forms.
# The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.
# Any Java object that can pass more than one IS-A test is considered to be polymorphic.
# Basically objects in python are more loosely used and do not have to be specified (such as in java).
# Python doesnt really care what TYPE something is, it is interested in the behaviour seen ie it passes the duck test-
# 'If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.'
# In the example below test_duck can be used on both the penguin and duck objects as they have the same calls available.


class Duck(object):

    def walk(self):
        print('waddle waddle waddle')

    def swim(self):
        print('come in the waters nice')

    def quack(self):
        print('quack quack')


class Penguin(object):

    def walk(self):
        print('I waddle')

    def swim(self):
        print('come in the waters freeeeeezin')

    def quack(self):
        print('er, I am a penguin, deeeerrrrrr')


def test_duck(duck):
    duck.quack()
    duck.swim()
    duck.walk()


if __name__ == ('__main__'):
    Donald = Duck()
    test_duck(Donald)

    percy = Penguin()
    test_duck(percy)
