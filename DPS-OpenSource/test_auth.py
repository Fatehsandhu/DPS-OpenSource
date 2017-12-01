import Functions
import os

def testFileName():
    assert Functions.fileName("data/file.txt") == "file.txt"

def testFileSize():
    path = "test_file.txt"
    path = os.path.join(os.path.dirname(__file__), path)
    assert Functions.fileSize(path) == 43