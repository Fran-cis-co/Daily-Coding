# -------------------------------------------------------------------------------------------------------------------------- #
# Given a string s containing just the characters '(', ')', '[', ]', '{', and '}', determine if the input string is valid
# An input string is valid if:
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order
#   3. Every close bracket has a corresponding open bracket of the same type
# -------------------------------------------------------------------------------------------------------------------------- #

#  Arrays to store the characters
curly = []
brackets = []
parenthesis = []

# Test cases
test1 = "()"
test2 = "()[]{}"
test3 = "(]"

#  -- Store characters into made databases -- #


def storeCharactersInDatabases(s):
    for x in s:
        storeCharactersInDatabasesHelper(x)


def storeCharactersInDatabasesHelper(character):
    if character == '(' or character == ')':
        parenthesis.append(character)
    elif character == '[' or character == ']':
        brackets.append(character)
    elif character == '{' or character == '}':
        curly.append(character)
# ------------------------------------------- #


def isValid():
    par = False
    bra = False
    curl = False
    for x in range(0, 3):
        if x == 0:
            par = validParenthesis()
        elif x == 1:
            bra = validBrackets()
        elif x == 2:
            curl = validCurly()

    if par and bra and curl:
        return True
    else:
        return False


def validParenthesis():
    if len(parenthesis) == 0:
        return True
    elif len(parenthesis) == 1:
        return False

    while (len(parenthesis) > 0):
        char = parenthesis.pop()
        if char == '(':
            try:
                parenthesis.remove(')')
            except:
                return False
        elif char == ')':
            try:
                parenthesis.remove('(')
            except:
                return False

    if len(parenthesis) == 0:
        return True
    else:
        return False


def validBrackets():
    if len(brackets) == 0:
        return True
    elif len(brackets) == 1:
        return False

    while (len(brackets) > 0):
        char = brackets.pop()
        if char == '[':
            try:
                brackets.remove(']')
            except:
                return False
        elif char == ']':
            try:
                brackets.remove('[')
            except:
                return False

    if len(brackets) == 0:
        return True
    else:
        return False


def validCurly():
    if len(curly) == 0:
        return True
    elif len(curly) == 1:
        return False

    while (len(curly) > 0):
        char = curly.pop()
        if char == '{':
            try:
                curly.remove('}')
            except:
                return False
        elif char == '}':
            try:
                curly.remove('{')
            except:
                return False

    if len(curly) == 0:
        return True
    else:
        return False


storeCharactersInDatabases(test3)
print(isValid())
