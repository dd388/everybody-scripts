# check size of file
# determine whether filesize is 0 bytes 
# write filesize to csv (question: do we want to do this for all files and sizes or only those with a filesize of 0?)

import sys, os

def validateFileSize(filename):
  filesize = os.path.getsize("/filepath")
  if filesize == 0:
    print("All files with 0 bytes")
    print (filename, "is", filesize, "bytes")

for filename in os.listdir(directory):
    validateFileSize(filename)

