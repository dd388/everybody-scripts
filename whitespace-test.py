#!/usr/bin/env python3
# attempt at removing whitespace from all filenames within a given directory


# determine whether filename includes whitespace 

import re
try:
    sp = re.compile('\s')
    findsp = sourcefile.find(sp)
    print "Error: file name contains whitespace"

# if whitespace is present, remove whitespace -- although, question for group: would we simply want the whitespace removed, or replaced with a dash or underscore?
import os
# https://stackoverflow.com/questions/41176509/python-how-to-replace-whitespaces-by-underscore-in-the-name-of-all-files-folde
def replace(parent):
    for path, folders, files in os.walk(parent):
        for f in files:
            os.rename(os.path.join(path, f), os.path.join(path, f.replace(' ', '_')))
        for i in range(len(folders)):
            new_name = folders[i].replace(' ', '_')
            os.rename(os.path.join(path, folders[i]), os.path.join(path, new_name))
            folders[i] = new_name

# if no whitespace is present, continue 



