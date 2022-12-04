### Create Database 
import sqlite3
conn = sqlite3.connect("people.db")
columns = [
"id INTEGER PRIMARY KEY",
"lname VARCHAR",
"fname VARCHAR UNIQUE",
"timestamp DATETIME",
]

table_check_s = "SELECT name FROM sqlite_master WHERE type='table' AND name='{person}'"

if not conn.execute(table_check_s):
    create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
    conn.execute(create_table_cmd)

    ## Populating database-> table person
    people = ["1, 'Hafiri', 'Majd', '2022-10-08 09:15:10'","2, 'Wick', 'Joe', '2022-10-08 09:15:13'","3, 'Ted', 'Smith', '2022-10-08 09:15:27'"]

    for person in people:
        insert_cmd = f"INSERT INTO person VALUES ({person})"
        conn.execute(insert_cmd)

conn.commit()