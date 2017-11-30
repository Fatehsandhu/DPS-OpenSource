#!/usr/bin/python
import os
import hashlib


path = "/Users/fatehsandhu/test.txt"

last = path.split('/')
last = last[-1]

print last

print os.path.getsize(path)

print("Sha 1 Digest")

hash_object = hashlib.sha1(path)
hex_dig = hash_object.hexdigest()
print(hex_dig)



print "End of functions"
