#!/usr/bin/env python3
# attempt at removing whitespace from all filenames within a given directory

# ask user to input filename
  # question for group -- this may not be the right place to ask for user input since presumably this would happen at the beginning of the script
  # also, we decided to do this for a single file to keep it simple. we can and should change this to a directory in the final script
sourcefile = input('Enter the file name:')


# determine whether filename includes whitespace 

import re
try:
    sp = re.compile('\s')
    findsp = sourcefile.find(sp)
    print "Error: file name contains whitespace"

# if whitespace is present, remove whitespace -- although, question for group: would we simply want the whitespace removed, or replaced with a dash or underscore?

# if no whitespace is present, continue 



