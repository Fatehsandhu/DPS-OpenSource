import Functions

def test_getFileName():
    assert Functions.fileName("data/file.txt") == "file.txt"