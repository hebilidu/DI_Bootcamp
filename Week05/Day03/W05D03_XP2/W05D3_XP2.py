# Week05 Day3 - OOP - XP Gold - Mini-project : Characters Game
# Created on  : 210504 by : lidu
# Modified on : 210504 by : lidu

#  
'''
Create a class called Character with the following attributes and methods:

    name
    life – starts with a default value of 20
    attack – the base attack of a character (integer) will be a default of 10
    basic_attack() - accepts another character as a parameter and will <attack> the character and the characters <life> points should drop.

Now create 3 different classes that inherit from Character:
Every character type should say (ie. print) something when they are created, get creative :)
    Druid:
        meditate() - increase life by 10, decrease attack by 2
        animal_help()- increase attack by 5
        fight() - accepts another character as a parameter and subtracts (0.75*life + 0.75*attack) from the other characters life.
        Example:
        druid.fight(other_char): other_char.life - (0.75*self.life + 0.75*self.attack)

    Warrior:
        brawl() - accepts another character as a parameter, subtacts (2*attack) to the other characters life and adds (0.5*attack) to his own life.
        train() - increase both your attack and life points by 2.
        roar() - accepts another character as a parameter and subtracts their attack points by 3.

    Mage:
        curse() – accepts another character as a parameter and subtracts their attack points by 2.
        summon() - increases attack attribute by 3 points.
        cast_spell() - accepts another character as a parameter and subtracts attack/life to the other characters life points (eg if your attack is 20 and life is 5 you will subtract 4 life points).

Once all your classes are created start testing them, create one of each character and use each of their methods.
'''
print('\nXP Gold - Mini-project : Characters Game\n=================')
