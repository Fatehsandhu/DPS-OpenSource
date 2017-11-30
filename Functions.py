#!/usr/bin/python
import os
import hashlib


path = "/Users/fatehsandhu/test.txt"

def fileName():
    last = path.split('/')
    last = last[-1]
    print last

# Gets the File Size
def fileSize():
    print os.path.getsize(path)


# The Hash Functions
def SHA():
    print("Sha 1 Digest")
    hash_object = hashlib.sha1(path)
    hex_dig = hash_object.hexdigest()
    print(hex_dig)

def MD5():
    print("MD5 Digest")
    hash_object = hashlib.md5(b'Hello World')
    print(hash_object.hexdigest())


print "End of functions"
