# Import relevant modules

import os
import fnmatch

# Using os.scandir, search all files within a given directory

with os.scandir('my_directory/') as entries:
    for file in entries:       
        
# Check to see if files contain whitespace using fnmatch
        if fnmatch.fnmatch(file, ' '):
           print(file, 'False')
        else
           print(file, 'True')

# Final step would be to output result to CSV - How do we do this?
# This only looks for whitespace in the file. Do we need to look for whitespace in the path?
# What about single/multiple whitespaces?
# how do we test this? Also - as written, you need to input the directory you're looking at. how does this function integrate into the larger script?



