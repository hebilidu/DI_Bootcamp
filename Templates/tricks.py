def is_alphanum(str):
    ''' Equivalent to built-in isalnum()
    codes 48 to 57: numeric (0-9) / 65 to 90: upper alpha (A-Z) / 97 to 122: lower alpha (a-z)
    '''
    for char in str:
        code = ord(char)
        if not (47 < code < 58 or 64 < code < 91 or 96 < code < 123):
            return False
    return True

def is_alpha(str):
    ''' Equivalent to built-in isalpha()
    codes 48 to 57: numeric (0-9) / 65 to 90: upper alpha (A-Z) / 97 to 122: lower alpha (a-z)
    '''
    for char in str:
        code = ord(char)
        if not(64 < code < 91 or 96 < code < 123):
            return False
    return True

def prompt_int_in_range(inf, sup):
    ''' Asks for and returns an integer within a range 
    '''
    number = None
    while type(number) is not int:
        try:
            return int(input(“Please enter a number between {} and {} : “.format(inf, sup)))
        except ValueError:
            print(“%s is not an integer.\n” % number)

# TIME
import datetime

present = datetime.datetime.now()
future = datetime.datetime(2022,1,1,0,0,0)
diff = future - present
days, hours, minutes = diff.days, diff.seconds // 3600, diff.seconds // 60 % 60
print(f"The delta between present and future is {days} days, {hours} hours and {minutes} minutes.\n")