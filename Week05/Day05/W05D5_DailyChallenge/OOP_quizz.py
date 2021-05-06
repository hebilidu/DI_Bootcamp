# Week05 Day5 - OOP - Daily challenge - OOP Quizz
# Created on  : 210506 by : lidu
# Modified on : 210506 by : lidu

# Part 1 : Quizz 
# Answer the following questions:

questions = {
'What is a class?': 
    'A class describes the properties of a group of objects and the actions that can be performed on them.', 
'What is an instance?': 
    'An instance is the occurrence of an object built from a specific class',
'What is encapsulation?': 
    'Encapsulaton consists in restricting direct variables and methods access in classes in order to prevent the accidental modification of data.',
'What is abstraction?': 
    'Abstraction consists in hiding the internal implementations of a process or method from the user. The user knows what work is being done  but not how it is being done.',
'What is inheritance?': 
    'Inheritance allows to  define a class that takes all the functionalities from a parent class and to add more',
'What is multiple inheritance?': 
    'When a class is derived from more than one base class,',
'What is polymorphism?': 
    'Polymorphism refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.',
'What is method resolution order or MRO?': 
    'It is a set of rules that determines the priority of application of classes inheritance. The parent classes are searched in a depth-first, left-right fashion and each class is searched once.'
}
def esc(code):
    return f'\033[{code}m'

for q, a in questions.items():
    print(esc('35;1'), q, esc(0))
    print(esc('35'), a, esc(0))

# Part 2: Create a deck of cards class.
# The Deck of cards class should inherit from a Card class.
# The requirements are as follows:
#  The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
#  The Deck class :
#    should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
#    should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
import random

class Deck():
    def __init__(self):
        suits = ('♠️','♥️','♦️','♣️')
        faces = ('a','2','3','4','5','6','7','8','9','10','j','q','k')
        self.deck = []
        for s in suits:
            for f in faces:
                self.deck.append((s,f))

    def __str__(self):
        out_str = ''
        for i in range(len(self.deck)):
            out_str += self.deck[i][1] + self.deck[i][0] + ((i+1) % 13 != 0)*' ' + ((i+1) % 13 == 0)*'\n'
        return out_str

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        '''Deals the top card of the deck'''
        card = self.deck.pop(0)
        return card[1]+card[0]

deck1 = Deck()
print('Initialized deck :')
print(deck1)
print('Shuffled deck :')
deck1.shuffle()
print(deck1)
print('dealt : ', deck1.deal())
print(deck1)