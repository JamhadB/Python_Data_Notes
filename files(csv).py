# This file explains how to work with csv files in python, using the star_classification file as an example

import csv

file = open("star_classification.csv", "r") # Opens the file for reading
file.close() # Closes the file

# or

 with open("star_classification.csv", "r") as file: # No need to close the file

# for writing new data to a csv file:

with open("data.csv", "w") as new_file:
    writer = csv.writer(new_file)
    writer.writerow(["trasaction_id", "product_id", "price"]) # Headings for table of data
    writer.writerow([1000, 1, 5]) # Data array
    writer.writerow([1001, 2, 15]) # Another data array

# For reading a csv file

with open("star_classification.csv") as file:
    reader = csv.reader(file)
    print(list(reader))  # Gets all data and converts it to a list object
    for row in reader:
        print(row)

# There is more to be explored here, especially considering this will be an important part of data analysis