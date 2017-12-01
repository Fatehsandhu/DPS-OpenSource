import Functions

def testFileName():
    assert Functions.fileName("data/file.txt") == "file.txt"

def testFileSize():
    assert Functions.fileSize("test_file.txt") == 43