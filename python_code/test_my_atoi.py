
from my_atoi import myAtoi


def test_my_atoi():
    string_and_expected = [
        ("", 0),
        (" ", 0),
        ("42", 42),
        ("   -42", -42),
        ("4193 with words", 4193),
        ("words and 987", 0),
        ("-91283472332", -2147483648),
        ("91283472332", 2**31 - 1),
    ]
    for string, expected in string_and_expected:
        assert myAtoi(string) == expected
