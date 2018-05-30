#!/usr/bin/env python3

# Import modules we need
    # What should we import to get the job(s) done?

# Rule: Does every file have an extension?
# Rule: Every file is at least zero bytes
# Rule: There are no hidden files here
# Rule: No filename has any sort of whitespace
    # What input does this need?
    # What should the output be?

# Output report
    # What input should this get to produce a report?
    # Does it produce the whole report or does it output line by line?

# Main function
def validator():
    pass
    # Some things we might want to do here:
        # Gather and check user input
        # Set up output filename (see if we're overwriting anything?)
        # Get a list of files we're working with
        # Run some rules and get feedback
        # Generate a report
    # Other things to think about
        # How should we handle unexpected input?
        # How do we write/run tests on this?

if __name__ == '__main__':
    validator()
    
import os

def getDirectory():
    targetDirectory = ('Enter the directory path: ')
    return targetDirectory

def validateExtension(filename):
    print("All files have extensions")

def validateFileSize(filename):
    print("All files bigger than 0 bytes")

def findHiddenFiles(filename):
    print("No hidden files found")
    
def findWhiteSpace(filename):
    print("No filenames contain whitespace")
    
targetDirectory = getDirectory()

filenames = os.listdir(targetDirectory)
print(filenames)

for filename in filenames:
    validateExtension(filename)
    validateFileSize(filename)
    findHiddenFiles(filename)
    findWhiteSpace(filename)
print("Done!")


*** *** 

sourcefile = input('Enter the directory name or file name:')

# Does this check if sourcefile is a directory or a single file? source: https://docs.python.org/3.0/library/stat.html
import os, sys
from stat import *

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname)[ST_MODE]
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)

for file in sourcefile:

# below assumes that all file names are separated with a comma
# the below pulls out the file extension and checks that it is valid, i.e. between 2 and 4 characters long

try:
  findext = sourcefile.find('.')
  ext = sourcefile.find(',',findext) #how to find end of a single file name, if no comma is present to separate multiple files
  fileext = sourcefile[findext:ext]
    if
      fileext == [2:4]
    elseif:
        print "Error: not a valid file extension"
   print fileext
except:
    print "Error: file does not have a file extension"

# the below searches for whitespace in filenames

space = sourcefile.find(' ')
    ' ' in sourcefile:
        if True:
        if False:

#finds whitespace in filenames with regular expressions

import re
try:
    sp = re.compile('\s')
    findsp = sourcefile.find(sp)
    print "Error: file name contains whitespace"


# the below tries to check the file size in bytes and print the file size. If the file is 0 bytes, it returns an error. Source: https://stackoverflow.com/questions/6591931/getting-file-size-in-python

try:
    def getSize(sourcefile):
    st = os.stat(sourcefile)
        if st.st_size == 0
            print "Error: file is 0 bytes"
        elseif:
            print st.st_size


