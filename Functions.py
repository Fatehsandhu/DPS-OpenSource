#!/usr/bin/python
import os
import hashlib


path = "/Users/fatehsandhu/test.txt"

last = path.split('/')
last = last[-1]

print last

print os.path.getsize(path)


print "End of functions"
