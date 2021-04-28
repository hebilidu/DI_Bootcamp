# Week04 Day04 - XP #1
# Created on  : 210428 by : lidu
# Modified on : 210428 by : lidu
import random

def main():
    '''  Exercise 1 : What are you learning ?
    Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
    Call the function, and make sure the message displays correctly.

    '''
    print('\nExercise 1\n==========')
    def display_message():
        print("Hey, I am learning Full Stack Web development at Developers.Institute.\n")
   
    display_message()

    
    ''' Exercise 2: What’s your favorite book ?
    Write a function called favorite_book() that accepts one parameter, title.
    The function should print a message, such as “One of my favorite books is Alice in Wonderland”.
    Call the function, make sure to include a book title as an argument when calling the function.

    '''
    print('\nExercise 2\n==========')
    def favorite_book(title):
        print("My favorite book is", title)
    
    favorite_book('Moby Dick, by Herman Melville')
   
    #  Exercise 3: Some Geography
    '''
    Write a function called describe_city() that accepts the name of a city and its country as parameters.
    The function should print a simple sentence, such as “Reykjavik is in Iceland”.
    Give the country parameter a default value.
    Call your function.

    '''
    print('\nExercise 3\n==========')
    def describe_city(city, country):
        print("{} is in {}".format(city, country))

    describe_city('Paris', 'France')
    describe_city('Barcelona', 'Spain (Catalunyia)')

    #  Exercise 4: Random
    print('\nExercise 4\n==========')
    '''Exercise 4 : Random
    Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
    Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
    '''
    def prompt_int_in_range(inf, sup):
        ''' Asks for and returns an integer within a range '''
        number = None
        while type(number) is not int:
            try:
                inp = int(input("Please enter a number between {} and {} : ".format(inf, sup)))
                if inf <= inp <= sup:
                    return inp
            except ValueError:
                print("%s is not an integer.\n" % number)

    def random_guess(n):
        guess = random.randint(1,100)
        if guess == n:
            return "Bravo, and unexpected !"
        else:
            return "You failed. Your number was {} and the guess is {}.".format(n, guess)

    while True:
        n = prompt_int_in_range(1, 100)
        print(random_guess(n) + '\n')
        inp = input('Another run (y/n)? ')
        if inp in ('n', 'N'):
            break


    #  Exercise 5: Let’s create some personalized shirts !
    print('\nExercise 5\n==========')
    '''
    Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
    The function should print a sentence summarizing the size of the shirt and the message printed on it.
    Call the function make_shirt() using positional arguments to make a shirt.
    Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
    Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
    Bonus: Call the function make_shirt() using keyword arguments.
    '''
    def make_shirt(size = 'L', txt = 'I love Python'):
        print('You have selected size {} and the text is "{}".'.format(size, txt))
    

    make_shirt('XL', 'Cocorico')
    make_shirt()
    make_shirt('M')

    # Exercise 6 : Magicians
    print('\nExercise 6\n==========')
    '''
    Make a list of magician’s names.
    Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
    Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
    Call the function make_great().
    Call the funcyion show_magicians() to see that the list has actually been modified.
    '''
    list_mag = ['Harry', 'Ron', 'Hermione', 'Neville', 'Dumbledore']
    def show_magicians(list):
        print(' 🧙‍♂️ '.join(list), '\n')

    def make_great(list):
        return [indiv + ' the Great' for indiv in list ]

    show_magicians(list_mag)
    show_magicians(make_great(list_mag))

if __name__ == "__main__":
    main()
