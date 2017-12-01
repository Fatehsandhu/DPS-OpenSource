#!/usr/bin/python
import os
import hashlib
import sys


path = "/Users/fatehsandhu/test.txt"

def fileName(path):
    last = path.split('/')
    return last[-1]

# Gets the File Size
def fileSize(path):
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
