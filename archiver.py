#! /usr/bin/env python3

import os, sys

def writeByteArray(fd):
    try:
        with open(fd, "rb") as f:
            byteArray = bytearray()
            byteArray += f.read()
            return byteArray
    except IOError:
        print("Error while opening file...")
        sys.exit(1)

#def readByteArray(fd):
    

path = "README.md"
if os.path.exists(path):
    byteArray = writeByteArray(path)
    print(byteArray)
else:
    print("File %s does not exist." % path)
    sys.exit(1)
print("\nDone...")
