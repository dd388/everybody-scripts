#Runs through a directory of files and identifies whether each file has an extension (true) or not (false).

import fnmatch
import os

def file_extension(file):
    if fnmatch.fnmatch(file, '*.*'):
        print(file, 'True')
    else:
        print(file, 'False')

for file in os.listdir('path/to/dir'):
    file_extension(file)
