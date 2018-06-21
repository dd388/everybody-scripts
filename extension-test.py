#!/usr/bin/env python3
# attempt at reporting whether or not files in a directory have extensions or not.

import os, csv, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o","--output", help="Path to and filename for the CSV to create.")
parser.add_argument("-d","--directory", help="Path to input directory.")
args = parser.parse_args()

if args.output:
	global csvOut
	csvOut = args.output
if args.directory:
	global inputDir
	inputDir = args.directory

with open (csvOut, 'w') as f: #'wb' worked in python 2.7. Does not in 3.5...somethign to do with 'wb' being write+binary, so expecting binary values not strings.
	writer = csv.writer(f)
	writer.writerow(['path','filename','extension','extPassFail'])
	for path, dirs, files in os.walk(inputDir):
		for filename in files:
			extension = os.path.splitext(filename)[1]
			if extension == "":
				extPassFail = "fail"
			else:
				extPassFail = "pass"
			writer.writerow([path,filename,extension,extPassFail])

