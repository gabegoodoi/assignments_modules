import text_utils as tu

'''
Objective: 
The aim of this assignment is to enhance your proficiency in using Python modules, both standard and custom, with a specific focus on importing with aliases.

Task 1: Custom Module with Aliases - Problem Statement: 

Create a custom module named `text_utils.py` with functions for string manipulation (e.g., reversing a string, capitalizing). In your main script, import this module using an alias and utilize its functions.

Code Example:

    # text_utils.py
    def reverse_string(s):
        # function to reverse a string

    def capitalize_string(s):
        # function to capitalize a string

    # main.py
    # Import text_utils using an alias and utilize its functions
- Expected Outcome: 
Your main script should be able to use the functions from `text_utils.py` via an alias, demonstrating an understanding of custom module creation and aliasing.

'''

text = input("Say what you need to say: ")

print(tu.capitalize(tu.reverse_string(text)))