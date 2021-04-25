# Week04 Day01 - XP Ninja - Exercises
# Created on  : 210425 by : lidu
# Modified on : 210425 by : lidu

def main():
    # Exercise 3 : Outputs
    print('Exercise 3\n==========')
    print(3 <= 3 < 9) # True
    print(3 == 3 == 3) # False -> True
    print(bool(0)) # False
    print(bool(5 == "5")) # Mix types error -> False
    print(bool(4 == 4) == bool("4" == "4")) # True
    print(bool(bool(None))) # error -> False
    # print(x = (1 == True)) # True -> error
    # print(y = (1 == False)) # error
    # print(a = True + 4) # 5 or error ? -> error
    # print(b = False + 10) # 10 or error ? => error
    # print("x is", x) # error x undefined
    # print("y is", y) # error y undefined
    # print("a:", a) # error
    # print("b:", b) # error

    # Exercise 4 : How many characters in a sentence ?
    print('\nExercise 4\n==========')

    my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
           Ut enim ad minim veniam, quis nostrud exercitation ullamco
           laboris nisi ut aliquip ex ea commodo consequat.
           Duis aute irure dolor in reprehenderit in voluptate velit
           esse cillum dolore eu fugiat nulla pariatur.
           Excepteur sint occaecat cupidatat non proident,
           sunt in culpa qui officia deserunt mollit anim id est laborum."""
    print('Length of my_text is {}'.format(len(my_text)))

    # Exercise 5: Longest word without a specific character
    # Keep asking the user to input the longest sentence they can without the character “A”.
    # Each time a user successfully sets a new longest sentence, print a congratulations message.
    print('\nExercise 5\n==========')
    longest = ''
    while True:
        inp = input('Enter a sentence without any "a" (empty will stop program): ')
        length = len(inp)
        if length == 0:
            break
        if 'a' in inp or 'A' in inp:
            continue
        else:
            if length > len(longest):
                longest = inp
                print('Congratulations. You have the highest score.')
    print('Longest sentence without an "a" is : ' + longest)


if __name__ == "__main__":
    main()
