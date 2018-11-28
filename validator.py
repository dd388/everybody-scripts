#!/usr/bin/env python3

# Import modules we need
    # What should we import to get the job(s) done?
import argparse # Definitely need a module like argparse if we want to supply arguments--f
from pathlib import Path

# Rule: if
# Rule: Does every file have an extension?
# Rule: Every file is at least zero bytes
# Rule: There are no hidden files here
def findHidden(f): #I'm assuming here that validator() is looping through files
    if f.startswith("."):
        print("!!!!! HIDDEN FILE FOUND !!!!!, ", f)

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
    if args.output:
        outputFile = args.output

    p = Path(inputDir) # declares inputDir as a Path object
    for i in p.glob('**/*.*'): # i in this statement should now be every file in p.
        print(i.name) # comment this line and make this loop do something else, like call one of our other functions

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
