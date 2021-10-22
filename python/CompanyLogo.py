
from collections import defaultdict
"""
Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
"""


def logo_selector(s: str):

    letter_occurences = defaultdict(lambda: 0)

    # Count em
    for letter in s:
        letter_occurences[letter] += 1

    # Sort em (by count then by alphabetical order)
    sorted_occurences = sorted(letter_occurences.items(),
                               key=lambda item: (-item[1], item[0]))

    logo = ""
    for i, pair in enumerate(sorted_occurences):
        if i < 3:
            logo += pair[0]
        else:
            break
    return logo
