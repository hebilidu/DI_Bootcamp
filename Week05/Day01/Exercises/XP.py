# Week05 Day1 - OOP - XP
# Created on  : 210502 by : lidu
# Modified on : 210502 by : lidu

# Exercise 1 : Cats
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def oldest_from_list(list):
    oldest = ['', 0]
    for indiv in list:
        if indiv.age > oldest[1]:
            oldest = [indiv.name, indiv.age]
    print(f'The oldest cat is {oldest[0]}, and is {oldest[1]} years old.')

cat1 = Cat(name='Felix', age=12)
cat2 = Cat(name='Tom', age=30)
cat3 = Cat(name='Alice', age=2)
oldest_from_list([cat1, cat2, cat3])


# Exercise 2 : Dogs
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def __str__(self):
        return f'{self.name} is {self.height} cm high.'
    def bark(self):
        print(f'{self.name} goes woof!')
    def jump(self):
        print(f'{self.name} jumps {self.height * 2} cm high.')
davids_dog = Dog('Rex', 50)
print(davids_dog)
davids_dog.bark()
davids_dog.jump()
sarahs_dog = Dog('Teacup', 20)
print(sarahs_dog)
sarahs_dog.bark()
sarahs_dog.jump()
if sarahs_dog.height > davids_dog.height:
    print(f'{sarahs_dog.name} is bigger')
else:
    print(f'{davids_dog.name} is bigger')

# Exercise 3 : Who’s the song producer?
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def __str__(self):
        return '/'.join(self.lyrics)
    def sing_me_a_song(self):
        print('\n'.join(self.lyrics))
# Create an object, for example:
stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# Then, call the sing_me_a_song method. The output should be:
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven
print(stairway)
stairway.sing_me_a_song()


# Exercise 4 : Afternoon at the Zoo
class Zoo:
    def __init__(self, name, animals=[]):
        self.name = name
        self.animals = animals
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    def get_animals(self):
        print(self.animals)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    def sort_animals(self):
        self.animals.sort()
        categories = {}
        key = 0
        for a in self.animals:
            if not categories: # set is empty
                key += 1
                categories[1] = [a]
            elif a[0] in categories.get(key)[0][0]:
                categories[key].append(a)
            else:
                key +=1
                categories[key] = [a]
        print(categories)
        return categories
    def get_groups(self, categories):
        for g in categories.values():
            print(g)
zoo1 = Zoo('Berne')
zoo1.add_animal('Emu')
zoo1.add_animal('Eel')
zoo1.add_animal('Cat')
zoo1.add_animal('Cougar')
zoo1.add_animal('Ape')
zoo1.add_animal('Bear')
zoo1.add_animal('Baboon')
zoo1.add_animal('Elephant')
print('\n' + zoo1.name)
zoo1.get_animals()
zoo1.sell_animal('Elephant')
zoo1.get_animals()
zoo1.get_groups(zoo1.sort_animals())

ramat_gan_safari = Zoo('Ramat Gan Safari',[])
print('\n' + ramat_gan_safari.name)

while True:
    a = input('Which animal do you wish to add (Just hit <Enter> when finished) : ')
    if a == '': break
    ramat_gan_safari.add_animal(a)

ramat_gan_safari.get_animals()
ramat_gan_safari.add_animal('Elephant')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Elephant')
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups(ramat_gan_safari.sort_animals())
