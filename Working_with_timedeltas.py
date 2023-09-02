# This file explains how to work with Time Deltas in python

from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()

duration = dt2 - dt1
print(duration)
print("days:",duration.days)
print("seconds:",duration.seconds)
print("total seconds:",duration.total_seconds())

# Everything about seems pretty self explanitory, hince the lack for comments. 'timedelta' can be used to make changes
# to an existing datetime or all to it:

dt3 = dt1 + timedelta(days=1, seconds=1000)
print(dt3)