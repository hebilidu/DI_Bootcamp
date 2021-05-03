# Week05 Day2 - OOP - XP+ exercises
# Created on  : 210503 by : lidu
# Modified on : 210503 by : lidu

# Exercise 1 : Family
l = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
]
class Family():
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

