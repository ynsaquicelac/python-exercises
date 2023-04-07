import pytest
from exercise1 import getFactorial
from exercise2 import searchPerson


@pytest.mark.parametrize("input,expected",
    [(5,120),
    (2,2),
    (0,1),
    ])
def test_factorial(input, expected):
    assert getFactorial(input) == expected


@pytest.mark.parametrize("input,expected",
    [("James","Doctor"),
    ("Anna","Person not found"),
    ])
def test_search_person(input, expected):
    assert searchPerson(input) == expected