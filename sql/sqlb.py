import sqlite3

with sqlite3.connect("real_shit.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('Los Angeles', \
        'CA', 10200000)")
    c.execute("INSERT INTO population VALUES('Portland', \
        'WA', 200000)")