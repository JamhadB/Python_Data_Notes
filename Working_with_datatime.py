# This file will explain how to work with datetime objects in python

from datetime import datetime

dt = datetime(2018, 1, 1) # Creates a datetime object with the year, month, and day passed as arguments. The hour, min,
                          # and second can also be passed.

datetime.now() # Returns the current datetime

datetime.strptime("2018/01/01", "%Y/%m/%d") # This is for parsing / converting a datetime string. Useful for when there
                                            # are inputs from a user or readings from a file.

# Googling 'python 3 strptime' will bring you the documentation for this method in order to learn the syntax for
# implementation

# We can also turn a time into a datetime object like so:

import time

dt = datetime.utcfromtimestamp(time.time())
print(dt)

print(f"{dt.year}/{dt.month}")

# We can also convert a datetime object into a string. (The opposite of .strptime):

print(dt.strftime("%Y/%m"))