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
        lower_case_vowels = ['a', 'e', 'i', 'o', 'u']
        result = ''.join([character.upper() if character in lower_case_vowels else character for character in self.string])
        return result
    
# make a user input for the string
user_input_string = input("Enter a string: ")

# instantiate the class and call the method
vowels_to_upper = VowelsToUpper(user_input_string)
result = vowels_to_upper.vowelsToUpper()

# print the result
print(result)

