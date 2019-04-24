#!/usr/bin/env python
import fnmatch


# defining a function
# returns True if it finds whitespace,
# returns False if not
def haswhitespace(fname):
    if fnmatch.fnmatch(fname, ' '):
        return(True)
    else:
        return(False)


filenames = ['directory/foo.txt', 'dir has space/this is fun.txt', 
             'nowhitespacehere.txt']

for bananas in filenames:
    returnedvalue = haswhitespace(bananas)
    print(returnedvalue)

