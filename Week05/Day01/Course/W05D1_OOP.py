# Week 05 Day 1 - OOP
class Animal():
    def __init__(self, legs, name):
        self.legs = legs
        self.name = name
        if not isinstance(legs, int):
            raiseTypeError('legs must be a number')

    def say_hello(self):
        print(f'{self.name} says hello')

    def add_height(self, height):
        self_height = height
        print('I\'ve got a height !!')

animal = Animal(legs=8, name='Charlotte')
animal2 = Animal(4, 'Sparky')
# animal3 = Animal('hello', 'Jules')
print(animal)
print(Animal)
print(animal.name)
print(animal2.name)
animal.say_hello()
animal2.say_hello()
print(isinstance(animal, Animal))
print(isinstance('animal', Animal))
animal.add_height(8)

class Car:
    def __init__(self, b, color, mn, ts):
        self.color = color
        self.brand = b
        self.model = mn
        self.top_speed = ts

my_car = Car(mn='Rover', b='Volkswagen', color='Red', ts=45.8)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

## create an instance of the class
p = Point(3,4)

## access the attributes
print("p.x is:", p.x)
print("p.y is:", p.y)

class Robot():
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f'Hey ! I am the robot {self.name}, I am {self.color} and I weigh {self.weight}')

r1 = Robot('Tom', 'red', 30)
r2 = Robot('Jerry', 'blue', 40)

r1.introduce_self()
r2.introduce_self()

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return(f'I belong to the Person class, with the name of {self.name}')

    def show_details(self):
        print("Hello my name is " + self.name)

    def modify_name(self, new_name):
        self.name = new_name

first_person = Person("John", 36)
first_person.show_details()
first_person.modify_name('Not John')
first_person.show_details()
print(first_person)
print(str(first_person))

class Computer():
    def description(self, name):
        """
        This is a totally useless function
        """
        print("I am a computer, my name is", name)
        #Analyse the line below
        print(self)

mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")
