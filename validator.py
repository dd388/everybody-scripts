#!/usr/bin/env python3

import argparse
import sys
import csv
from pathlib import Path

# Testing functions go here
# Input: path to file
# Output: True or False



# Main function
def validator():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--directory",
                        help="Path to input directory. If unused, " + 
                             "input will be current directory.")
    parser.add_argument("-o","--output",
                        help="Path to and filename for output file. " + 
                             "If unused, output will be to stdout")
    args = parser.parse_args()

    if args.directory:
        inputDir = Path(args.directory)
        if not inputDir.is_dir():
            sys.exit("Exiting: Input directory not valid.")
    else:
        print("No input directory specified. Using current directory: ")
        print(Path.cwd())
        print("") # spacing is friendly.
        inputDir = Path.cwd()
    if args.output:
        outputTarget = Path(args.output)
        if outputTarget.exists():
            print("Input file already exists.")
            print("Do you want to overwrite this file?")
            overwrite = None
            while overwrite not in ('y', 'n'):
                overwrite = input("Please enter yes or no. ")
                overwrite = overwrite[0].casefold()
                if overwrite == 'y':
                    outputFile = open(outputTarget, 'w')
                elif overwrite == 'n':
                    sys.exit("Exiting: Will not overwrite existing file.") 
                else:
                    pass # user didn't remotely answer the question.
            print("") # spacing is still friendly.
        else:
            outputFile = open(outputTarget, 'w')
    else:
        outputFile = sys.stdout

    print("TESTS:")
    print("inputDir : ", inputDir)
    print("outputFile : ", outputFile)


    # TODO: Identify files in inputDir
    #       Create a loop for them
    #       Run each test, get and store True/False values
    #       Write a CSV (use the CSV module)
    #       Good job.

if __name__ == '__main__':
    validator()
