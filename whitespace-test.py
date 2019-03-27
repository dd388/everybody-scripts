# Define an input (e.g. a directory of files)
# Check to see if file contains whitespace
    # If it does contain whitespace, the file fails
    # If it does NOT contain whitespace, the file passes
# Loop through all files in directory
# Output result to CSV

# STEPS: 1) Understand Farrell's code; 2) Look at Shira/Maggie's code to see if there's anything there to re-use 3) What is the final product in the context of the larger script 4) Do the work


# -- IGNORE BELOW; IT IS OLD --






#!/usr/bin/env python3
# -*- coding: utf-8 -*-
    # question for group: what if the files we're working with are not encoded in UTF-8?
# attempt at removing whitespace from all filenames within a given directory


# determine whether filename includes whitespace 
    # question for group: is this something we actually want the function to do? like, is it necessary?

import re
try:
    sp = re.compile('\s')
    findsp = sourcefile.find(sp)
    print "Error: file name contains whitespace"

# if whitespace is present, changes whitespace to underscore
    # although, question for group: do we event want to change the filenames, or do we just want to generate a report that says they don't conform to our specs? 
    # if we do change the filenames, would we simply want the whitespace removed, or replaced with a dash or underscore?
# source: https://stackoverflow.com/questions/41176509/python-how-to-replace-whitespaces-by-underscore-in-the-name-of-all-files-folde
# this changes both parent folder names and children file names
import os

def replace(parent):
    for path, folders, files in os.walk(parent):
        for f in files:
            os.rename(os.path.join(path, f), os.path.join(path, f.replace(' ', '_')))
        for i in range(len(folders)):
            new_name = folders[i].replace(' ', '_')
            os.rename(os.path.join(path, folders[i]), os.path.join(path, new_name))
            folders[i] = new_name

# run replace function

# output result to csv



