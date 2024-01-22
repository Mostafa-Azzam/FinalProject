import _sqlite3

conn = _sqlite3.connect('madeupdatabase.db')

c = conn.cursor()

#c.execute("""CREATE TABLE human(
#              firstName TEXT,
#              lastName TEXT,
#              age INTEGER
#    )""")


c.execute("INSERT INTO human VALUES ('Mostafa', 'Abdelaziz', 101)")
c.execute("INSERT INTO human VALUES ('Mohab', '', 100)")
c.execute("INSERT INTO human VALUES ('Joshua', '', 100)")

c.execute("SELECT * FROM human WHERE age = 100")

print(c.fetchall())

conn.commit()
conn.close()