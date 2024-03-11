# Given an integer x, return true if x is a palindrome and false otherwise.

# --- Test cases --- #
# x = 121
# x = -121
x = 10


def isPalindrome(num):
    return str(num) == str(num)[::-1]


print(isPalindrome(x))
