# This file explains how to work with SQLite in python. SQLite is a very lightweight database used for storing data
# on an application. Usually used for apps on mobile devices.

import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())
print(movies)

#with sqlite3.connect("db.sqlite3") as conn: # creates a database named 'db.sqlite3' opens it as 'conn' for connection
    #command = "INSERT INTO Movies VALUES(?, ?, ?)" # Create an sql command to do things with the 'Movies' table
    #for movie in movies: # Iterate over movies list
        #conn.execute(command, tuple(movie.values())) # For each movie, we'd execute this command
    #conn.commit() # All changes will be written to the database. Only needed for when writing to a database.

# First running this code returns an error because the 'Movies' table does not exist. The table would first need to be
# created. Googling 'db browser for sqlite' brings you to a website to open the sqlite database and look at it's content.

# I've downloaded the application and written the data to the created table. We can read the data from the database like
# so:

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies" # Gets everything from the movies table
    cursor = conn.execute(command)
    for row in cursor:
        print(row)

# There is more to explore here. I commented out the first lines of code as once exicuted, the table was alread created
# can now be read with the second chunck. Knowing SQL commands helps here quite a bit.