'''
Given a text file file.txt that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.
'''

# Use the open() function to read the text file
with open('193-ValidPhoneNumbers/file.txt') as f:
    # Since the open() functions returns as an iterable object, iterate through it 
    for line in f:
        # If the number contains 2 hyphens, then it is a valid number,
        # If the number contains () and one hyphen, it is also valid
        if (line.count("-") == 2):
            # Use .strip() to remove the white space
            print(line.strip())
        elif line.count("-") == 1 and line.count("(") == 1 and line.count(")") == 1:
            print(line.strip())
