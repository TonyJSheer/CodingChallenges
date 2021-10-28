
import re


regex_integer_in_range = r"[1-9]\d{5}$"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"  # Do not delete 'r'.

P = "552523"
print(bool(
    re.match(regex_integer_in_range, P)
))

P = "552523"
print(bool(
    re.match(regex_integer_in_range, P)
) and len(
    re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
)
