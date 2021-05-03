# Week 05 Day 2 - OOP

# find classes from which a class inherits
class A():
    pass

class B(A):
    pass

import inspect
print(inspect.getmro(B))
print(inspect.getmro(A))
print(inspect.getmro(object))
print(inspect.getmro(list))
# print(inspect.getmro(sequence))


class MyClass(object):
    def func(self):
        print("I'm being called from the Parent class")


class ChildClass(MyClass):
    def func(self):
        print("I'm actually being called from the Child class")
        print("But.......")
        # Calling the `func()` method from the Parent class.
        super().func()

my_instance_2 = ChildClass()
my_instance_2.func()

class A(B):
    def __init__(self, *args, **kwargs):
        B.__init__(self, *args, **kwargs)
        # super().__init__(self, *args, **kwargs)
        pass

# Door exercise
class Door():
    def __init__(self, is_opened=False):
        self.is_opened = is_opened
    def open_door(self):
        self.is_opened = True
    def close_door(self):
        self.is_opened = False

class BlockedDoor(Door):
    def open_door(self):
        print("Door is blocked. Can't open it.")

    def close_door(self):
        print("Door is blocked. Can't close it.")


# Exceptions
my_list = [2, 3, 1, 2, "four", 42]
valid_list = [2, 3, 1, 2, 42]

class MyPersonalException (Exception):
    pass

def try_to_sum(a_list):
    try:
        print(sum(a_list))
        raise MyPersonalException('Arbitrary exception !')
    except Exception as e: 
        print("List contains invalid numbers")
        print(e)

try_to_sum(my_list)
try_to_sum(valid_list)
 
     