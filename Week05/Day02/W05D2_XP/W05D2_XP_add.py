# Week05 Day2 - OOP - XP exercises
# Created on  : 210503 by : lidu
# Modified on : 210503 by : lidu

# Exercise 3 : Dogs Domesticated
'''
Create a new python file and import your Dog class from the previous exercise.
In the new python file, create a class named PetDog that inherits from Dog.
Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
Add the following methods:
    train: prints the output of bark and switches the trained boolean to True

    play: takes a parameter which value is a few names of other dogs (use *args). The method should print the following string: “dog_names all play together”.

    do_a_trick: If the dog is trained the method should print one of the following sentences at random:
        “dog_name does a barrel roll”.
        “dog_name stands on his back legs”.
        “dog_name shakes your hand”.
        “dog_name plays dead”.
'''

from W05D2_XP import Dog
from random import choice

class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained
    def train(self):
        self.bark()
        self.trained = True
    def play(self, *args):
        list_dogs = [self.name]
        for indiv in args:
            list_dogs.append(indiv.name)
        print('\n' + ', '.join(list_dogs) + ' all play together\n')
    def do_a_trick(self):
        trick_list = [" does a barrel roll", " stands on back legs" , " gives paw", " plays dead"]
        if self.trained:
            print(f"\n{self.name}{choice(trick_list)}\n")

print("\nExercise 3 : Dogs Domesticated\n==============================")
dog10 = PetDog('Alfred', 4, 24, True)
dog11 = PetDog('Brady', 6, 8)
dog12 = PetDog('Carmen', 11, 19)
dog10.play(dog11, dog12)
dog10.play()
dog11.train()
dog11.do_a_trick()