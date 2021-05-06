# Week05 Day5 - OOP - Daily challenge - Modules
# Created on  : 210506 by : lidu
# Modified on : 210506 by : lidu

# Using the requests and time modules, create a function which returns the amount of time 
# it takes a webpage to load (how long it takes for a complete response to a request).
# Test your code with multiple sites such as google, ynet, imdb, etc.

import time
import requests
# import urllib.error

def measure_req_completion_time(url):
    try:
        start = time.time()
        r = requests.get(url)
        roundtrip = time.time() - start
    except:
        print("Something is wrong with your url. Make sure ist starts with https:// or http://.")
    else:
        print(round(roundtrip, 2), 's')

url1 = 'https://api.chucknorris.io/jokes/random'
url2 = 'https://google.com'
url3 = 'http://google.com'
url4 = 'https://imdb.com'

for url in [url1, url2, url3, url4]:
    print(url)
    measure_req_completion_time(url)

while True:
    url = input("Enter a valid url (nothing to exit): ")
    if len(url) == 0:
        print("n\Program ends... Thanks for playing with us.\n")
        break
    measure_req_completion_time(url)
