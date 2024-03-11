#  Given a roman numeral, convert it to an integer

#  Data base to find the roman and integer equivalents
symbols = ["I", "V", "X", "L", "C", "D", "M"]
values = [1, 5, 10, 50, 100, 500, 1000]

#  Test Cases
test1 = "III"  # Output should be 3
test2 = "LVIII"  # Output should be 58
test3 = "MCMXCIV"  # Output should be 1994

# print(symbols[0][1])


# Method to do the calculation of converting the roman number to an integer
def romanToInt(roman):
    #  Variable to keep the converted integer from roman to integer
    sum = 0

    # Have an index to start at the first letter of the roman string
    x = 0
    #  Use while loop since we can break out of it once we have iterated through the entire string
    while x < len(roman):
        firstIndex = symbols.index(roman[x])
        if x != len(roman) - 1:
            secondIndex = symbols.index(roman[x + 1])

        # If the current iterated letter in the string is greater than the one towards the right, add it straight to the sum variable
        if (firstIndex >= secondIndex):
            sum += values[firstIndex]
            x += 1
        else:
            # If the letter is less than the one on the right, subtract the right letter from the current iterated letter and move to the unchecked letter
            sum += values[secondIndex] - values[firstIndex]
            x += 2

    return sum


# Method call
sum = romanToInt(test3)
print(sum)
