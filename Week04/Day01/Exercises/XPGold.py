# Week04 Day01 - XP Gold - Exercises
# Created on  : 210425 by : lidu
# Modified on : 210425 by : lidu

def main():
    # Exercise 1 : Hello World-I love Python
    print('Exercise 1\n==========')
    print('Hello world\n' * 4 + 'I love Python\n' * 4 )

    # Exercise 2 : What is the Season ?
    print('Exercise 2\n==========')
    month = int(input('Please enter a month (1-12) : '))
    if 0 < month < 13:
        if 3 <= month <=5:
            print('Spring !')
        elif 6 <= month <= 8:
            print('Summer !')
        elif 9<= month <= 11:
            print('Autumn !')
        else:
            print('Winter !')

if __name__ == "__main__":
    main()
