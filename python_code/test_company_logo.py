
from company_logo import logo_selector


def test_logo_selector():
    test_input = "aabbbccde"
    expected = "bac"
    result = logo_selector(test_input)
    assert result == expected


if __name__ == "__main__":
    test_logo_selector()
