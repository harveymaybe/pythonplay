	#insert multiple records using a tuple
import sqlite3

with sqlite3.connect("real_shit.db") as connection:
	c = connection.cursor()    
	cities = [
            ('Boston', 'MA', 600000),
            ('Chicago', 'IL', 2700000),
            ('Houston', 'TX', 2100000),
            ('Phoenix', 'AZ', 1500000)
            ]

    # insert data into table
	c.executemany("INSERT INTO population VALUES(?, ?, ?)",cities)