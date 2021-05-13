# Week 06 Day 5 - Daily Challenge - API to DB

# 1. Using this API, create the functionality which will write 10 random countries to your database.
# 2. These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.

import requests
import json
import random
import sqlite3 as sl

def get_countries():
    '''returns a list of dictionaries'''
    url = 'https://restcountries.eu/rest/v2/all?fields=name;capital;flag;subregion;population'
    data = requests.get(url)
    data = data.json()
    return data

def extract_random_countries(n):
    '''random choice of n countries. Return list of n dictionaries'''
    return random.sample(get_countries(), n)

def add_list_to_db(list_countries):
    '''Expects a list of dictionaries as input.'''
    connection = sl.connect('country.db')
    cursor = connection.cursor()
    for c in list_countries:
        query = f"INSERT INTO country (name, capital, flag, subregion, population) VALUES ('{c['name']}', '{c['capital']}', '{c['flag']}', '{c['subregion']}', {c['population']});"
        try:
            query_result = cursor.execute(query)
        except:
            print(f"{c['name']} is already in database. Skipped.")
    connection.commit()
    connection.close()

add_list_to_db(extract_random_countries(10))