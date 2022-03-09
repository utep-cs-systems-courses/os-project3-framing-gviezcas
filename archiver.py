#! /usr/bin/env python3

import os, sys
#Method to turn file into byte array.#
def writeByteArray(fd):
    try:
        with open(fd, "rb") as f:
            byteArray = bytearray()
            byteArray += f.read()
            return byteArray
    except IOError:
        print("Error while opening file...")
        sys.exit(1)

        
#Method to turn byte array back into file.#
def readByteArray(fd, byteArray):
    try:
        with open(fd, "wb") as f:
            f.write(byteArray)
    except IOError:
        print("Error while opening file...")
        sys.exit(1)

def archiver(byteArray):
    size = len(byteArray)
    sizeString = str(size)
    sizeOfSize = len(sizeString)
    byteArray[0:0] = sizeString.encode()
    return_tuple = (byteArray, sizeOfSize)
    return return_tuple

#Below is just to test the methods above using the README file.#
#print("Attempting to archive file...\n")
#try:
#    os.remove("test.md")
#except:
#    pass
#path = "README.md"
#if os.path.exists(path):
#    byteArray = writeByteArray(path)
#    archiver(byteArray)
#    print(byteArray)
#    print("---------------------------------------------------------------")
#    print("Attempting to unarchive file...\n")
#    readByteArray("test.md", byteArray)
#    try:
#        with open("test.md", 'r') as f:
#            print(f.read())
#    except FileNotFoundError:
#        print("File could not be found or open...")
#        sys.exit(1)
#else:
#    print("File %s does not exist." % path)
#    sys.exit(1)
#print("\nDone...")
#sys.exit(0)
