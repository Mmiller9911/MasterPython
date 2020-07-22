# a class is a blueprint for an object
# a class has a default constructor (without adding the __init__)
# using the . to access methods or variables is called dot notation
# the self keyword is the same as this in java
# a function which is defined in a class is called a method instead
# a variable which is defined in a class is called an attribute
# an attribute can be added to a class instance by assigning a variable to it but then this would not be present for other class instances
# class names start with upper-case + camelcase by convention
# a leading underscore indicates that the method is not intended to be used outside the class
# a @staticmethod can be added using the tag, this is then called using the classname.methodnme
# it is NOT required to have classes in different files in python, usually you would store all the classes in one file, it can be done if required though.
# in python 3 all classes are a subclass of the object superclass, the object does not have to be declared like "class Kettle(object)" but this is because "class Kettle" is a shortcut to do the same thing.


class Kettle(object):

    power_source = 'electricity'  # class variable
    class_number = 55  # class variable

    def __init__(self, make, price):  # self is just the current instance object, for self just think 'object'
        print('I am called automatically when a new instance is created')
        self.make = make
        self.price = price  # instance variable
        self.on = False
        self.number_1 = 0
        self.number_2 = 0
        print(self)

    def switch_on(self):
        self.on = True

    def practice(self):
        self.number_1 = 7
        self.number_2 = 51
        print('concatenating: ' + str(self.number_1) + str(self.number_2) + str(self.class_number))
        print('hello' + self.power_source + Kettle.power_source)  # self.power_source is just the same as kettle.power_source
        return str(self.make) + str(self.price)


kenwood = Kettle('kenwood', 9.96)
print(kenwood.price)
kenwood.price = 5.50
print(kenwood.price)
print(kenwood.switch_on())
print(kenwood.practice())

hamilton = Kettle('hamilton', 20)
print(hamilton.price)
print(Kettle.power_source)
print('makes are {} = {}, {} = {}'.format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))
print('makes are {0.make} = {0.price}, {1.make} = {1.price}'.format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

kenwood.power = 1.5
print(kenwood.power)

print('switch to atomic')
Kettle.power_source = 'atomic'
kenwood.power_source = 'gas'
print(Kettle.power_source)
print(kenwood.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)

#  ============================================================================================================================================

import datetime
import pytz


class Account:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    """ Simple account class with balance """
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = [((Account._current_time(), balance))]
        print('Account created for ' + self._name)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
           # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount)) # store a tuple in list
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print('Balance must be valid')
        self.show_balance()

    def show_balance(self):
        print('Balance is {}'.format(self._balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0 :
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1 # tranlates - 50 to 50  amount = -50 * -1 = 50 - two negatives make a positive
            print(' {:6} {} on {} (local time was {})'.format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    matt = Account('Matt', 0)
   # matt.show_balance()

    matt.deposit(100)
    matt.withdraw(50)
    matt.show_transactions()

    Steph = Account('Steph', 800)
    Steph.deposit(100)
    Steph.withdraw(200)
    Steph.show_transactions()

#  ============================================================================================================================================

