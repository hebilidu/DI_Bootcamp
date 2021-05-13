import requests
import json
import sqlite3 as sl
from faker import Faker
from time import time

def gen_fake_data(n):
    start = time();
    f = Faker()
    connection = sl.connect('fake-date.db')
    cursor = connection.cursor()
    for i in range(n):
        name = f.name()
        email = f.email()
        query = f"INSERT INTO fake ('name', 'email') VALUES ('{name}','{email}');"
        query_result = cursor.execute(query)  #Cursor runs the query
    connection.commit()  #Finalize the result. "Write" it to the DB
    connection.close()
    end = time();
    print(f"The function ran in {round(end-start,2)}s")

gen_fake_data(1000)