# Week04 Day02 - XP - Exercises
# Created on  : 210426 by : lidu
# Modified on : 210426 by : lidu

def main():
    #  Exercise 1 : Favorite numbers
    # Create a set called my_fav_numbers with all your favorites numbers.
    # Add two new numbers to the set.
    # Remove the last number.
    # Create a set called friend_fav_numbers with your friend’s favorites numbers.
    # Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
    print('Exercise 1\n==========')
    my_fav_numbers = {13, 8}
    print('my_fav_numbers', my_fav_numbers)
    print('type of my_fav_numbers', type(my_fav_numbers))
    my_fav_numbers.add(42)
    my_fav_numbers.add(404)
    print('my_fav_numbers after some adds', my_fav_numbers)
    my_fav_numbers.pop()
    print('my_fav_numbers after pop', my_fav_numbers)
    friend_fav_numbers = {12, 7, 1}
    print('friend_fav_numbers', friend_fav_numbers)
    our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
    print('our_fav_numbers', our_fav_numbers)

    #  Exercise 2: Tuple
    print('Exercise 2\n==========')
    print('Given a tuple which value is integers, is it possible to add more integers to the tuple?')
    print('Not directly, but it is possible to use tuples addition')
    tuple1 = ('mango', 'orange')
    print('tuple1 :', tuple1)
    a = 'banana'
    tuple1 = tuple1 + (a,)
    print('tuple1 :', tuple1)

    #  Exercise 3: Print a range of numbers
    # Use a for loop to print all numbers from 1 to 20, inclusive.
    print('Exercise 3\n==========')
    for i in range(1, 21):
        print(i)

    # Exercise 4: Floats
    # Recap – What is a float? What is the difference between an integer and a float?
    # Can you think of another way to generate a sequence of floats?
    # Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
    print('Exercise 4\n==========')
    list4 = []
    for i in range(2, 6):
        list4.append(i - 0.5)
        list4.append(i)
    print(list4)

    # Exercise 5: Shopping List
    # Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
    # Remove “Banana” from the list.
    # Remove “Blueberries” from the list.
    # Add “Kiwi” to the end of the list.
    # Add “Apples” to the beginning of the list.
    # Count how many apples are in the basket.
    # Empty the basket.
    # Print(basket)
    print('Exercise 5\n==========')
    basket = ["Banana", "Apples", "Oranges", "Blueberries"]
    print('basket : ', basket)
    basket.remove('Banana')
    print('basket after removing "Banana" : ', basket)
    basket.remove('Blueberries')
    print('basket after removing "Blueberries" : ', basket)
    basket.append('Kiwi')
    print('basket after adding "Kiwi" : ', basket)
    basket.insert(0, 'Apples')
    print('basket after adding "Apples" at the beginning : ', basket)
    count = 0
    for item in basket:
        if item == 'Apples':
            count += 1
    print('Number of apples in basket : ', count)
    basket = []
    print('basket : ', basket)

    # Exercise 6 : Loop
    print('Exercise 6\n==========')
    # Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
    inp_name = ''
    while inp_name != 'Lien':
        inp_name = input('Please enter a name ("Lien" to stop): ')
        print('Hello,', inp_name)

    # Exercise 7
    print('Exercise 7\n==========')
    # Given a list, use a loop to print out every element which has an even index
    list7 = input('Please enter a list of items : ').split()
    print("list7 :", list7)
    for item in list7:
        print(item)

    # Exercise 8
    print('Exercise 8\n==========')
    # Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
    for i in range(1500, 2501):
        if i % 5 == 0 and i % 7 == 0:
            print(i)

    # Exercise 9: Favorite fruits
    print('Exercise 9\n==========')
    # Ask the user to input their favorite fruit(s) (one or several fruits).
    # Hint : Use the built in input method. Ask the user to separate the fruits with a single space,
    # eg. "apple mango cherry".
    # Store the favorite fruit(s) in a list (convert the string of words into a list of words).
    # Now that we have a list of fruits, ask the user to input a name of any fruit.
    #     If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
    #     If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
    list9 = input('Please enter our favorite fruits (separated by spaces): ').split()
    fruit = input('Now, name a fruit : ')
    if fruit in list9:
        print('You chose one of your favorite fruits! Enjoy!')
    else:
        print('You chose a new fruit. I hope you enjoy')

    # Exercise 10: Who ordered a pizza ?
    print('Exercise 10\n==========')
    # Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop
    # asking for toppings.
    # As they enter each topping, print a message saying you’ll add that topping to their pizza.
    # Upon exiting the loop print all the toppings on the pizza pie and what the total price is
    # (10 + 2.5 for each topping).
    price = 10
    top_list = []
    while True:
        topping = input ('Add a topping ("quit" when finished) : ')
        if topping == "quit":
            break
        elif len(topping) > 0:
            top_list.append(topping)
            price += 2.5
    print('Good choice ! Here are your toppings :', top_list)
    print(' And the cost is :', price)

    # Exercise 11: Cinemax
    print('Exercise 11\n==========')
    # A movie theater charges different ticket prices depending on a person’s age.
    #     if a person is under the age of 3, the ticket is free.
    #     if they are between 3 and 12, the ticket is $10.
    #     if they are over the age of 12, the ticket is $15.
    # Ask a family the age of each person who wants a ticket.
    # Store the total cost of all the family’s tickets and print it out.
    # A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people
    # between the ages of 16 and 21.
    # Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch
    # the movie.
    list11 = input('Enter ages separated with spaces : ').split()
    total = 0
    num1, num2, num3 = 0, 0, 0
    for age in list11:
        if int(age) < 3:
            num1 += 1
        if 3 <= int(age) < 12:
            num2 += 1
            total += 10
        elif int(age) >= 12:
            num3 += 1
            total += 15
    print ('So: {} under 3, {} between 3 and 12, {} over 12 makes ${}'.format(num1, num2, num3, total))

    # Exercise 12 : Who is under 16?
    print('Exercise 12\n==========')
    # Given a list of names, write a program that asks every user for their age, if they are less
    # than 16 years old remove them from the list.
    # At the end, print the final list.
    list12 = ['Johnny', 'Bill', 'Tom']
    list12_copy = list12.copy()
    for name in list12:
        age = input('{} !, how old are you ? '.format(name))
        if int(age) < 16:
            list12_copy.remove(name)
    print("Remaining people are:", list12_copy)

    # Exercise 13
    print('Exercise 13\n==========')
    # Make a list called sandwich_orders and fill it with the names of various sandwiches .
    # Then make an empty list called finished_sandwiches.
    # As each sandwich is made, move it to the list of finished sandwiches.
    # After all the sandwiches have been made, print a message listing
    # each sandwich that was made , such as I made your tuna sandwich.
    sandwich_orders = ['pastrami', 'falafel', 'pastrami', 'shwarma', 'falafel']
    finished_sandwiches = []
    while len(sandwich_orders) != 0:
        sand = sandwich_orders[0]
        print('{} is ready !'.format(sand))
        finished_sandwiches.append(sand)
        sandwich_orders.remove(sand)
    print(finished_sandwiches)

    # Exercise 14
    print('Exercise 14\n==========')
    # Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list
    # at least three times.
    # Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
    # and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
    # Make sure no pastrami sandwiches end up in finished_sandwiches.
    sandwich_orders = ['pastrami', 'falafel', 'pastrami', 'pastrami', 'shwarma', 'falafel']
    finished_sandwiches = []

    print('Sorry, we are out of patrami sandwiches.')
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    while len(sandwich_orders) != 0:
        sand = sandwich_orders[0]
        print('{} is ready !'.format(sand))
        finished_sandwiches.append(sand)
        sandwich_orders.remove(sand)
    print(finished_sandwiches)

if __name__ == "__main__":
    main()
