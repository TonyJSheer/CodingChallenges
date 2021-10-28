
"""
In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
In the second line, print True if s has any alphabetical characters. Otherwise, print False.
In the third line, print True if s has any digits. Otherwise, print False.
In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
In the fifth line, print True if s has any uppercase characters. Otherwise, print False.
"""

s = "54353465"

# first, try checking each character
has_alphanumeric = any(char.isalnum() for char in s)
print(has_alphanumeric)
has_alphabetic = any(char.isalpha() for char in s)
print(has_alphabetic)
has_digit = any(char.isdigit() for char in s)
print(has_digit)
has_lower = any(char.islower() for char in s)
print(has_lower)
has_upper = any(char.isupper() for char in s)
print(has_upper)

# This is 5 loops, try to condense
alphanumeric = 1
alphabetic = 2
digit = 3
lower = 4
upper = 5

things_to_check = [
    alphanumeric, alphabetic, digit, lower, upper
]

for char in s:
    if not things_to_check:
        break
    for condition in things_to_check:
        if condition == alphanumeric:
            if char.isalnum():
                things_to_check.remove(alphanumeric)

        elif condition == alphabetic:
            if char.isalpha():
                things_to_check.remove(alphabetic)

        elif condition == digit:
            if char.isdigit():
                things_to_check.remove(digit)

        elif condition == lower:
            if char.islower():
                things_to_check.remove(lower)

        elif condition == upper:
            if char.isupper():
                things_to_check.remove(upper)

print(alphanumeric not in things_to_check)
print(alphabetic not in things_to_check)
print(digit not in things_to_check)
print(lower not in things_to_check)
print(upper not in things_to_check)
