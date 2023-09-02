# This file explains how to work with Zip files in python

from pathlib import Path
from zipfile import ZipFile

zip = ZipFile("files.zip", "w") # Code for writing to a zip file. Also creates the file if it does not exist
for path in Path("ecommerce").rglob("*,*"):
    zip.write(path) # Takes all files from the ecommerce directory and writes them to the zip file

zip.close() # Closes the file

# There is a cleaner way to do this

with ZipFile("files.zip", "w") as zip:
    for path in Path("ecommerce").rglob("*,*"):         # With this, we no longer need to call the close method
        zip.write(path)

# To read the conent of the zip file:

with ZipFile("files.zip") as zip:
    zip.namelist() # Returns a list of all the files in the zip file
    info = zip.getinfo("Pass address of file") # Returns an info object
    info.file_size # Returns the size of the file
    info.compress_size # Compresses the size of the file (if possible)
    zip.extractall("directory") # Extracts all the files from a zip file. A different directory can be passed as an argument
                     # for where the files should go