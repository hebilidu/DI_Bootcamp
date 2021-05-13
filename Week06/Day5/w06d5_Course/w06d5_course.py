import psycopg2
import psycopg2.extras
import sys

HOSTNAME = '127.0.0.1'
USERNAME = 'lidu'
PASSWORD = sys.argv[1]
DATABASE = 'dvdrental'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )

# cursor = connection.cursor()
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

query = "SELECT * FROM customer LIMIT 20;"

cursor.execute(query)

results = cursor.fetchall()

connection.close()

for item in results:
    print(item)

