# check size of file
# determine whether filesize is 0kb or >0kb
# write filesize to csv? (question: do we want to do this for all files and sizes or only those with a filesize of 0?)

import sys
import os

filename = f in files
def validateFileSize(filename):
  filesize = os.path.getsize("/filepath")
  if filesize > 0
    print("All files bigger than 0 bytes")
    print (filename, "is", filesize, "bytes")

For filename is os.listdir(directory):
    for filename
        validateFileSize


## other bits of code and notes
        def getSize(filename):
            st = os.stat(filename)
            return st.st_size
