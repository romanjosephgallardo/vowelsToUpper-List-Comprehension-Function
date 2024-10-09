'''
## Lab exercise 3
### Provide a list comprehension that implementation for a function called vowelsToUpper with the following signature:

method name : vowelsToUpper

input argument : String 

return argument : String

vowelsToUpper must return a version of its String argument with all its vowels changed to their uppercase forms. Nonvowel characters stay as is.

### Sample Calls

vowelsToUpper "" == ""

vowelsToUpper "Hello, world!" == "HEllO, wOrld!"

vowelsToUpper "hello hi bye" == "hEllO hI byE"
'''

# pseudocode

# define a class called vowelsToUpper that takes a string as input
class VowelsToUpper:
    def __init__(self, string):
        self.string = string
    # define a function called vowelsToUpper that takes a string as input
    def vowelsToUpper(self):
        # create a list of vowels
        vowels = ['a', 'e', 'i', 'o', 'u']
        # create a list of uppercase vowels
        upper_vowels = ['A', 'E', 'I', 'O', 'U']
        # convert the string to a list of characters
        string_list = list(self.string)
        # create a list comprehension that checks if the character is a vowel
        if character in string_list in vowels:
            # if the character is a vowel, convert it to uppercase
            character = character.upper()
            return character

# make a user input for the string
# instantiate the class and call the method
# print the result


