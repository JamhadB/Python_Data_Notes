# This files explains how to work with json (JavaScript Object Notation) files in python
# Facebook, Twitter, Youtube, and Yelp all provide their data in jason format
# Personal websites can provide their data in json format as well

import json

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},          # Data array in a 'movies' object
    {"id": 2, "title": "Kindergarten Cop", "year": 1993}
]

data = json.dumps(movies) # Takes the 'movies' data and formats it as json
print(data, "<--data")

# The 'data' variable is a string that can be written to a file:

from pathlib import Path

Path("movies.json").write_text(data) # Creates a 'movies.json' file and writes the 'data' to it

# For reading a json file:

data2 = Path('movies.json').read_text()
movies2 = json.loads(data2)   # Parse the 'data2' string into an array of objects
print(movies2, "<--data2")

# Square brackets can also be used to specify a specific piece of information:

print(movies2[0]['title']) # Example