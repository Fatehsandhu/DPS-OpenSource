#!/usr/bin/python
import os
import hashlib


# Gets the File Name
def fileName(path):
    last = path.split('/')
    return last[-1]

# Gets the File Size
def fileSize(path):
    return os.path.getsize(path)


# The Hash Functions
def SHA(path):
    print("Sha 1 Digest")
    hash_object = hashlib.sha1(path)
    hex_dig = hash_object.hexdigest()
    return hex_dig

def MD5(path):
    print("MD5 Digest")
    hash_object = hashlib.md5(path)
    return hash_object.hexdigest()