![JacobEM](https://jacobem.com/assets/media/JacobEM.png)

# Character In Sentence

CharInSentence is a Python library for examining whether character(s) are found within a string. You can compare your string against default alphabets or your own custom list.

![Version: 2.0](https://img.shields.io/badge/Version-2.0-00e0a7)

![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC--BY--SA-776bff)
## Documentation

### How to use

```py
import charInSentence
charInSentence.check(See-Parameter-One, See-Parameter-Two, See-Parameter-Three)
```

#### Reference One

| Parameter | Description                |
| :-------- | :------------------------- |
| `1` | Lower & upper case alphabet |
| `2` | Lower case alphabet |
| `3` | Upper case alphabet |
| `4` | Lower & upper case alphabet and numbers 0-9 |
| `5` | Lower case alphabet and numbers 0-9 |
| `6` | Upper case alphabet and numbers 0-9 |
| `Type(List)` | Pass a list for your own custom list |


#### Reference Two

The sentence that the character list is compared to. (Input as a string)


#### Reference Three

Should the program ignore spaces in the sentence or not? (Input True or False)

### Notes
If the program finds character(s) that are not in the sentence it will return them. Return Type: List

If the program doesn't find any character(s) not in the sentence it will return True. Return Type: Boolean

### Examples

```py
charInSentence.check(['t', 'x'], 'test', False)
# Would return ['x'] as x is not found within 'test'


charInSentence.check(1, 'abcdefghijklmnop', False)
# Would return ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] as we are checking lower case letters alphabet letters


charInSentence.check(['t', 'e'], 'test', False)
# Would return True as both 't' and 'e' are found within 'test'
```
