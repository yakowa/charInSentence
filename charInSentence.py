'''
Character in Sentence

HOW TO USE
import charInSentence
charInSentence.check(See-Reference-One, See-Reference-Two, See-Reference-Three)


REFERENCE ONE
Characters list that is compared to the sentence.
(Use 1 for lower and upper case alphabet)
(Use 2 for lower case alphabet)
(Use 3 for upper case alphabet)
(Use 4 for lower and upper case alphabet + numbers 0-9)
(Use 5 for lower case alphabet + numbers 0-9)
(Use 6 for upper case alphabet + numbers 0-9)
(Use a list for your own custom list)

REFERENCE TWO
Sentence that the character list is compared to.
(Input as a string)

REFERENCE THREE
Should the program ignore spaces in the sentence or not?
(Use True or False)


If the program finds character(s) that are not in the sentence it will return them.
Return-Var-Type: list

If the program doesn't find any character(s) not in the sentence it will return True.
Return-Var-Type: bool


EXAMPLES
charInSentence.check(['t', 'x'], 'test', False)
# Would return ['x'] as x is not found within 'test'

charInSentence.check(1, 'abcdefghijklmnop', False)
# Would return ['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] as we are checking lower case letters alphabet letters

charInSentence.check(['t', 'e'], 'test', False)
# Would return True as both 't' and 'e' are found within 'test'



Made by:
https://JacobEM.com/software?q=charInSentence


Licensed under CC BY-SA 4.0
'''

def check(var0, var1, var2):
    # Checking mode for the character list.
    if var0 == 1:
        characterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    elif var0 == 2:
        characterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    elif var0 == 3:
        characterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    elif var0 == 4:
        characterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    elif var0 == 5:
        characterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    elif var0 == 6:
        characterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    elif isinstance(var0, list):
        characterList = var0
    else:
        raise Exception('Character list is not set keys (1-6) or a custom list.')


    # Checking if sentence is a string and valid.
    if isinstance(var1, str) and len(var1) > 0:
        sentenceString = var1
    else:
        raise Exception('Sentence string is not a string or is 0 characters long.')


    # Checking if spaces are allowed or not.
    if isinstance(var2, bool):
        if var2 == True:
            characterList.append(' ')
    else:
        raise Exception('Allow-Spaces boolean is not a boolean.')


    # Main Algorithm

    # Turning the sentence string into a list.
    sentence = []
    for char in sentenceString:
        sentence.append(char)
    
    charErrors = []
    for char in characterList:
        if not char in sentence:
            charErrors.append(char)
    
    if len(charErrors) > 0:
        return charErrors
    else:
        return True