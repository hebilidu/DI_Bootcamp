# Week04 Day01 - XP - Exercises
# Created on  : 210425 by : lidu
# Modified on : 210425 by : lidu

def main():
    # Exercise 1 : Hello World
    # Print the following output in one line of code:
    #     Hello world
    #     Hello world
    #     Hello world
    #     Hello world
    print('Exercise 1\n==========')
    print('Hello world\n' * 4)

    # Exercise 2 : Some Math
    #     Write code that calculates the result of: (99^3) * 8
    print('Exercise 2\n==========')
    print('Note: ^ is the binary operator XOR')
    print('(99^3) * 8 = {}'.format((99 ^ 3) * 8))

    # Exercise 3 : What is the output ?
    #     Predict the output of the following code snippets:
    print('\nExercise 3\n==========')
    # >>> 5 < 3 # False
    print('Outcome of 5 < 3 is {}'.format(5 < 3))
    # >>> 3 == 3 # True
    print('Outcome of 3 == 3 is {}'.format(3 == 3))
    # >>> 3 == "3" # False
    print('Outcome of 3 == "3" is {}'.format(3 == "3"))
    # >>> "3" > 3 # not sure... -> TypeError
    #    print('Outcome of "3" > 3 is {}'.format("3" > 3))
    # >>> "Hello" == "hello" # False
    print('Outcome of "Hello" == "hello" is {}'.format("Hello" == "hello"))

    # Exercise 4 : Your computer brand
    #     Create a variable called computer_brand which value is the brand name of your computer.
    #     Using the computer_brand variable print a sentence that states the following:
    #     "I have a <computer_brand> computer".
    print('\nExercise 4\n==========')
    computer_brand = 'Apple'
    print('I have an {} computer.'.format(computer_brand))

    # Exercise 5 : Your information
    #     Create a variable called name, and set it’s value to your name.
    #     Create a variable called age, and set it’s value to your age.
    #     Create a variable called shoe_size, and set it’s value to your shoe size.
    #     Create a variable called info and set it’s value to an interesting sentence about yourself.
    #     The sentence must contain all the variables created in parts 1, 2 and 3.
    #     Have your code print the info message.
    #     Run your code
    print('\nExercise 5\n==========')
    name = 'Lien'
    age = 55
    shoe_size = 7
    info = 'My name is {}, I am {} years old and my shoe_size is {}.'.format(name, age, shoe_size)
    print(info)

    # Exercise 6 : A & B
    #     Create two variables, a and b.
    #     Each variables value should be a number.
    #     If a is bigger then b, have your code print Hello World.
    print('\nExercise 6\n==========')
    a = 1
    b = 2
    if a > b:
        print('Hello World')
    else:
        print('Goodbye World')

    # Exercise 7 : Odd or Even
    #     Write code that asks the user for a number and determines whether this number is odd or even.
    print('\nExercise 7\n==========')
    num = input('Please enter an integer : ')
    if int(num) % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'
    print('{} is {}'.format(num, odd_or_even))

    # Exercise 8 : What’s your name ?
    #     Write code that asks the user for their name and determines whether or not you have the same name,
    #     print out a funny message based on the outcome.
    print('\nExercise 8\n==========')
    your_name = input('Enter our name : ')
    if your_name == name:
        print('Wow, we\'ve got the same name. Good for you !')
    else:
        print('Nope, our names are different. Maybe next time.')

    # Exercise 9 : Tall enough to ride a roller coaster
    #     Write code that will ask the user for their height in inches.
    #     If they are over 145cm print a message that states they are tall enough to ride.
    #     If they are not tall enough print a message that says they need to grow some more to ride.
    print('\nExercise 9\n==========')
    height_inch = input('What is your height (in inches) ? ')
    height_cm = float(height_inch) * 2.54
    print('That would be {} cm'.format(height_cm))
    if height_cm > 145:
        print('You are tall enough to ride.')
    else:
        print('You need to grow some more to ride.')


if __name__ == "__main__":
    main()
