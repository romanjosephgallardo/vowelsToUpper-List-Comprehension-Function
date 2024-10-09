# Vowels to Upper

# Define a class called vowelsToUpper that takes a string as input
class VowelsToUpper:
    def __init__(self, string):
        self.string = string
    # Define a function called vowelsToUpper that takes a string as input
    def vowelsToUpper(self):
        lower_case_vowels = ['a', 'e', 'i', 'o', 'u']
        # Use list comprehension to change the vowels to uppercase
        result = ''.join([character.upper() if character in lower_case_vowels else character for character in self.string])
        return result
    
# Make a user input for the string
user_input_string = input("Enter a string: ")

# Instantiate the class and call the method
vowels_to_upper = VowelsToUpper(user_input_string)
output = vowels_to_upper.vowelsToUpper()

# Print the result
print(output)

