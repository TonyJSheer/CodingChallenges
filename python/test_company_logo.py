from CompanyLogo import logo_selector
import pytest


def test_logo_selector():
    test_input = "aabbbccde"
    expected = "bac"
    result = logo_selector(test_input)
    assert result == expected

if __name__ == "__main__":
    test_logo_selector()
