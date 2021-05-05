# is_alphanum
# is_alpha
# prompt_int_in_range
# diff_between_dates
# Translate text from file
# random_chuck_norris

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
def diff_between_dates():
    present = datetime.datetime.now()
    future = datetime.datetime(2022,1,1,0,0,0)
    diff = future - present
    days, hours, minutes = diff.days, diff.seconds // 3600, diff.seconds // 60 % 60
    print(f"The delta between present and future is {days} days, {hours} hours and {minutes} minutes.\n")

# Translate text from file
from translate import Translator

def translate_from_file(file, from, to='ja'):
    translator = Translator(to_lang = to)
    try:
        with open('./test.txt', mode='r') as my_file:
            text = my_file.read()
            translation = translator.translate(text)
            with open('./test-ja.txt', mode='w') as my_out_file:
                my_out_file.write(translation)
    except FileNotFoundError as e:
        print('Check file path')

# API get Chuck Norris jokes
import requests

def random_chuck_norris():
    response = requests.get("https://api.chucknorris.io/jokes/random")

    data = response.json()

    def esc(code):
        return f'\033[{code}m'

    print(f"\nChuck Norris random joke:\n", esc('31;1'), data['value'], esc(0), "\n")
