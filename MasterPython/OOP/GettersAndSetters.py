# Are not required for accessing instance objects in python but can still be used if desired.
# Basically they use a method for accessing data objects on a class object but this can be done without them in python.
# The property value should NEVER have the same name as the data attribute it references or it will break the code.
# The property value creates an instance of the property class

# The str method is useful for a string representation of the object, either when someone codes in str(your_object) ,
# or even when someone might do print(your_object).
# The str method is one that should be the most human-readable possible, yet also descriptive of that exact object.
#
# The @property and @score.setter are an alternate approach to properties which can be used (to creating a member of the property class)


class Player(object):

    def __init__(self, name):
        self.name = name
        self._level = 1
        self._lives = 3  # the underscore indicates that the user shouldn't be using this property (but still can)
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print('lives cannot be less than zero')
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level >= 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print('level cannot be less than one')
            self._level = 0

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self): # since an object is passed in then it is easy to get the data of it
        return 'Name {0.name}, Level: {0._level}, Lives: {0._lives}, Score: {0.score} '.format(self)