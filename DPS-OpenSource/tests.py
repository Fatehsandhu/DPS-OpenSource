import Functions

def test_getFileName():
    assert Functions.fileName("gg/hello\something/file.exe") == "file.exe"