from python.CompanyLogo import logo_selector
import pytest

def test_logo_selector():
    test_input = "aabbbccde"
    expected = "abc"
    assert logo_selector(test_input) == expected
