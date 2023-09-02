# This file explains how to work with timestamps in python

import time

time.time() # Returns the current datetime as a time stamp (Number of seconds since the beginning of time for the os)

# Because the time is not human readable, it is typically used for calculations. An example is displayed below:

def send_emails():
    for i in range(10000):
        pass

start = time.time()             # This calculation tells how long it takes for this fuction to execute.
send_emails()
end = time.time()
duration = end - start
print(duration)