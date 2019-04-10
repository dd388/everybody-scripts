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



