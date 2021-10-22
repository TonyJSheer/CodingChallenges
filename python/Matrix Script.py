import re

n, m = 5, 9

matrix = [
    '#%$r%r$n ',
    'O%Mi$iTi$',
    'yiaxsprt ',
    'est%ctiy#',
    '  t c i %'
]


ordered_characters = [
    matrix[i][j]
    for j in range(m)
    for i in range(n)
]

ordered_string = ''.join(ordered_characters)


# Replace non-alpha-numeric between alpha-numeric with ' '
to_replace = re.findall(r"\b\W+\b",  ordered_string)

for gap in to_replace:
    ordered_string = ordered_string.replace(gap, ' ', 1)
print(ordered_string)

a = 2 + 3
