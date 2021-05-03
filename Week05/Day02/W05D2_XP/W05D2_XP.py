# Week05 Day2 - OOP - XP exercises
# Created on  : 210503 by : lidu
# Modified on : 210503 by : lidu

# Exercise 1 : Pets
'''
Create another cat breed. In order to do so, create a class which inherits from the Cat class.
Create a few cat instances.
Create a list called my_cats, which will hold all the created cat instances.
Create a variable called my_pets. It’s value is an instance of the Pet class.
Hint : Use the my_cats variable to create the instance.
Take all the cats for a walk, use the walk method.

'''
print('\nExercise 1 : Cats\n=================')
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

cat01 = Bengal('Albert', 5)
cat02 = Bengal('Bernie', 10)
cat03 = Chartreux('Carlita', 6)
cat04 = Siamese('Dorothy', 17)
cat05 = Siamese('Emilio', 2)
my_cats = [cat01, cat02, cat03, cat04, cat05]
my_pets = Pets(my_cats)
my_pets.walk()


# Exercise 2 : Dogs
'''
Create a class called Dog with the following attributes name, age, weight.
Implement the following methods in the Dog class:
    bark: returns a string which states: “<dog_name> is barking”.
    run_speed: returns the dogs running speed (weight/age*10).
    fight : takes a parameter which value should be another dog called other_dog, returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

Create 3 dogs and run them through your class.
'''
print('\nExercise 2 : Dogs\n=================')
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        print(f"{self.name} is barking")
    def run_speed(self):
        return self.weight / self.age * 10
    def fight(self, other_dog):
        if self.run_speed() > other_dog.run_speed():
            print(f"{self.name} wins !")
        elif self.run_speed() < other_dog.run_speed():
            print(f"{other_dog.name} wins !")
        else:
            print("It's a tie !")
dog01 = Dog('Arnie', 8, 30)
dog02 = Dog('Bear', 9, 45)
dog03 = Dog('Cooper', 5, 30)
dog01.bark()
dog02.bark()
dog03.bark()
dog01.run_speed()
dog02.run_speed()
dog03.run_speed()
dog01.fight(dog01)
dog01.fight(dog02)
dog02.fight(dog03)
