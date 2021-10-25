

def myAtoi(s: str) -> int:
    """
    1Read in and ignore any leading whitespace.
    2Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    3Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    4Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    5If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    6Return the integer as the final result.
    Note:

    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
    """

    # 1/ strip whitespace
    s = s.lstrip(' ')

    # 2/ handle +/- sign
    negative = False
    if not s:
        return 0
    if s[0] == '-':
        negative = True
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    # 3/ get rid of 0's, and return 0 if no legal digits found
    if not s:
        return 0
    while s[0] and s[0] == '0':
        s = s[1:]
        if not s:
            return 0

    # 4/ now start reading in digits!
    digits = []
    for digit in s:
        if digit.isdigit():
            digits.append(int(digit))
        else:
            break

    if not digits:
        return 0

    # construct number!
    number = 0
    for i, digit in enumerate(digits[::-1]):
        number += digit * (10 ** i)
    if negative:
        number = -number

    # 5/ cap integer
    lower, upper = (-(2**31), 2**31 - 1)
    if number > upper:
        number = upper
    elif number < lower:
        number = lower

    return number
