# this is NOT recommended but can be done with:
from OOP.Polymorphism import Duck


# def add_duck(self, duck: Duck) -> None:
#     if type(duck) is Duck:
#         self.flock.append(duck)


# BUT - If required then the below version should be used as this includes subclasses.  This can be useful for stuff like checking an int has been sent to a method but this is not really pythonic, pythonic is more about behaviour than object type.
#
# def add_duck(self, duck: Duck) -> None:
#     if isinstance(duck, Duck):
#         self.flock.append(duck)
#
#
# class Malard(Duck):
#     pass
#
# percy = ducks.Malard()
#
# THIS IS THE CORRECT WAY TO DO IT - PYTHONIC AND CHECKS BEHAVIOUR - if it quacks like a duck then it is a duck
#
def add_duck(self, duck: Duck) -> None:
    fly_method = getattr(duck, 'fly', None) # check if the attribute exists on the variable - will return none instead of a not present error
    if callable(fly_method):                # check if the variable is callable, methods and functions are callable and attributes aren't
        self.flock.append(duck)             # if the object can fly then add it to the flock
    else:
        raise TypeError('cannot add duck, are you sure it is not a ' + str(type(duck).__name__))