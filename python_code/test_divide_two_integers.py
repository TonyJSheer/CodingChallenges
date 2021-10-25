
from divide_two_integers import divide


def test_divide():
    dividends_divisors_results = [
        (10, 3, 3),
        (7, -3, -2),
        (0, 1, 0),
        (1, 1, 1),
        (-(2**31), 1, -(2**31)),
        (-2147483648, -1, 2147483647)
    ]
    for dividend, divisor, expected in dividends_divisors_results:
        assert divide(dividend, divisor) == expected
