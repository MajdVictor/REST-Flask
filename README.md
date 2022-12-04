create people table on sqlite3
>>> import sqlite3
>>> conn = sqlite3.connect("people.db")
>>> columns = [
"id INTEGER PRIMARY KEY",
"lname VARCHAR",
"fname VARCHAR UNIQUE",
"timestamp DATETIME",
]
>>> create_table_cmd = f"CREATE TABLE person ({','.join(columns)})"
>>> conn.execute(create_table_cmd)
