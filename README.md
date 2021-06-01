<p align="center">
	<a href="https://jacobem.com" target="_blank">
		<img width="400px" src="https://jacobem.com/assets/media/JacobEM.png" alt="Yakowa">
	</a>
</p>

# Character in Sentence
CharInSentence is a Python library for examining whether character(s) are found within a string. You can compare your string against default alphabets or your own custom list.

### Licensed under CC BY-SA 4.0

## HOW TO USE
<code>import charInSentence</code>
<br>
<code>charInSentence.check(See-Reference-One, See-Reference-Two, See-Reference-Three)</code>


### REFERENCE ONE
Characters list that is compared to the sentence.
<br>
(Use 1 for lower and upper case alphabet)
<br>
(Use 2 for lower case alphabet)
<br>
(Use 3 for upper case alphabet)
<br>
(Use 4 for lower and upper case alphabet + numbers 0-9)
<br>
(Use 5 for lower case alphabet + numbers 0-9)
<br>
(Use 6 for upper case alphabet + numbers 0-9)
<br>
(Use a list for your own custom list)

### REFERENCE TWO
Sentence that the character list is compared to.
(Input as a string)

### REFERENCE THREE
Should the program ignore spaces in the sentence or not?
(Use True or False)

### NOTE
If the program finds character(s) that are not in the sentence it will return them.
Return-Var-Type: list

If the program doesn't find any character(s) not in the sentence it will return True.
Return-Var-Type: bool


## EXAMPLES
<code>charInSentence.check(['t', 'x'], 'test', False)</code>
<br>
Would return ['x'] as x is not found within 'test'

<code>charInSentence.check(1, 'abcdefghijklmnop', False)</code>
<br>
Would return ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] as we are checking lower case letters alphabet letters

<code>charInSentence.check(['t', 'e'], 'test', False)</code>
<br>
Would return True as both 't' and 'e' are found within 'test'
