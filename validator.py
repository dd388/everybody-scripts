#!/usr/bin/env python3

# Import modules we need
import argparse # Definitely need a module like argparse if we want to supply arguments--f
from pathlib import Path

# Rule: Does every file have an extension?
# Rule: Every file is at least zero bytes
# Rule: There are no hidden files here
def findHidden(f): #I'm assuming here that validator() is looping through files
    if f.startswith("."):
        return True
    else:
        return False

# Rule: No filename has any sort of whitespace
    # What input does this need?
    # What should the output be?

# Output report
    # What input should this get to produce a report?
    # Does it produce the whole report or does it output line by line?

# Main function
def validator():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--directory", help="Path to input directory. If unused, input will be current directory.")
    parser.add_argument("-o","--output", help="Path to and filename for output file. If unused, output will be to stdout")
    args = parser.parse_args()

    if args.directory:
        inputDir = args.directory
    else:
        pass # TODO Make current directory
    if args.output:
        outputFile = args.output
    else:
        pass # TODO Make stdout

    p = Path(inputDir) # declares inputDir as a Path object
    for i in p.glob('**/*.*'): # i in this statement should now be every file in p.
        print(i.name) # comment this line and make this loop do something else, like call one of our other functions
        findHidden(i) # for each file (i), return True if it's a hidden file, return false if it's not a hidden file

if __name__ == '__main__':
    validator()
