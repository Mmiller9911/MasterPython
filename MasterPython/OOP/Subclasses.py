# allow subclasses to inherit all the data/methods of the superclass
# allow subclasses to override the behaviour of the superclass if needed
# if inheriting from another class and both the constructors do not need any arguments then will connect be default but
# if the parent requires some information then it must be passed by the child


from OOP.GettersAndSetters import Player


class Enemy:

    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True
        self.initial_points = hit_points

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print('I took {} damage and have {} remaining points'.format(damage, self.hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                print('{0.name} lost a life'.format(self))
                self.hit_points = self.initial_points
            else:
                print('{0.name} died'.format(self))
                self.alive = False

    def __str__(self):
        return 'Name: {0.name}, Hit points: {0.hit_points}, Lives: {0.lives},'.format(self)

#  ============================================================================================================================================


class Troll(Enemy):
    # def __init__(self, name):
    #     Enemy.__init__(self, name=name, hit_points=23, lives=1)
    # def __init__(self, name):
    #     super(Troll, self).__init__(name=name, hit_points=23, lives=1) # call the base constructor (__init) of Enemy using, the class name and the object
    def __init__(self, name):
        super().__init__(name=name, hit_points=23, lives=1) # call the base constructor (__init) of Enemy

    def troll_grunt(self):
        print('Me {0.name}. {0.name} will stomp you good!!!'.format(self))


class Vampire(Enemy):
    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=3) # call the base constructor (__init) of Enemy

#  ============================================================================================================================================

# from oopsdemo import calendar
# from filename import classname

#  ============================================================================================================================================


tim = Player('tim')

# print(tim.name)
# tim.lives -=1
# print(tim)
# tim._set_level(2)
# print(tim._get_level())
# tim.level += 5
# print(tim._get_level())
# tim.level = 3

# random_monster = Enemy('Bert', 12, 1)
# print(random_monster)
#
# random_monster.take_damage(4)
# print(random_monster)
# random_monster.take_damage(9)
# print(random_monster)

# ugly_troll = Troll('pat')
# print('Ugly troll is {}'.format(ugly_troll))
#
# another_troll = Troll('another')
# print('Another troll is {}'.format(another_troll))
#
brother_troll = Troll('BrotheyMcDo')
# print('Brother Troll is {}'.format(brother_troll))
#
# brother_troll.troll_grunt() # this method exists for trolls only
# brother_troll.take_damage(1000)
# print(brother_troll)
# brother_troll.take_damage(9)
# print(brother_troll)
#
dracula = Vampire('Dracula')
print(dracula)
# dracula.take_damage(6)
# print(dracula)

while dracula.alive:
    dracula.take_damage(1)
    print(dracula)
    print('-' * 50)