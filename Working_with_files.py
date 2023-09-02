# This file explains how working with files in python goes

# Useful methods for working with files:

from pathlib import Path

path = Path("ecommerce/__init__.py") # Shows path to file we'd like to inquire about
print(path.exists()) # Ask if the file in question exist
path.rename() # Allows us to rename the file in question
path.unlink() # Allows us to delete the file in question
path.stat() # Returns information about the file

# st_size is the size of the file in bytes
# st_atime is the last access time
# st_mtime is the last modify time      All time values are in seconds after epic. This means that are seconds after the
# st_ctime is the creation time         start of time on a computer. These times are platform dependent.

from time import ctime # This is the module that will allow us to change the seconds after epic time into human time
ctime(path.stat().st_ctime) # This is the code to veiw the creation time in human time

path.read_bytes # This returns the content of the file 'as applied to objects when representing binary data
path.read_text # This returns the content of a file as a string

# There are two way to copy and move files

source = Path("ecommerce/__init__.py") # File to be copied
target = Path() / "___init__.py" # Created path for the file to go

source.read_text() # Reads the content of the source
target.write_text() # Writes the content to the target
target.write_text(source.read_text()) # This is the code likes put together

# The other (better) way is as follows:

import shutil

shutil.copy(source, target) # Does the same thing as the above code without all the words