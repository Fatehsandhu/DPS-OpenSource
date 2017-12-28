# DPS-OpenSource

### Table Of Contents

Links to the various files

| File | Path |
| ------ | ------ |
| Main Functions File  | [Functions.py](https://github.com/Fatehsandhu/DPS-OpenSource/blob/master/DPS-OpenSource/Functions.py) |
| Test file | [test_auth.py](https://github.com/Fatehsandhu/DPS-OpenSource/blob/master/DPS-OpenSource/test_auth.py) |
| License | [MIT](License.md)  |

### Functions Implemented in [Functions.py](https://github.com/Fatehsandhu/DPS-OpenSource/blob/master/DPS-OpenSource/Functions.py)

| Function | Description |
| ------ | ------ |
| fileName(path)  | Gets the filename from the entire URL |
| fileSize(path) | Gets the size of the file |
| SHA(path) | Creates the SHA1 hash |
| MD5(path) | Creates the MD5 hash |

[Functions.py]: <https://github.com/Fatehsandhu/DPS-OpenSource/blob/master/DPS-OpenSource/Functions.py>
[test_auth.py]: <https://github.com/Fatehsandhu/DPS-OpenSource/blob/master/DPS-OpenSource/test_auth.py>
[License.txt]: <https://github.com/Fatehsandhu/DPS-OpenSource/blob/master/License.txt>

### Example

```python
# Get SHA hash
hash = SHA('/DPS-OpenSource/test_file.txt'):

# print the SHA hash value
print hash
```

The following table is a collection of functionalities that need to be implemented.

#### Params

- **String** `path`: The path to the file you want.

| Function Name | Description | Input | Expected Output
| ----- | ----- | ----- | ----- |
| `fileName(path)` | Filename without the path | `test_file.txt` | `test_file.txt` |
| `fileSize(path)` | File size in bytes | `test_file.txt` | 44 Kb |
| `SHA(path)` | SHA1 digest for a file at the given path | The quick brown fox jumps over the lazy dog | 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 |
| `MD5(path)` | MD5 digest for a file at the given path | The quick brown fox jumps over the lazy dog | 9e107d9d372bb6826bd81d3542a419d |

## License
This project is licensed under the [MIT](License.md) license.
