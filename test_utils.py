import pytest
from utils import get_square, is_prime, get_greeting


def test_get_square():
    assert get_square(2) == 4
    assert get_square(-3) == 9
    assert get_square(0) == 0


def test_is_prime():
    assert is_prime(7) is True
    assert is_prime(4) is False
    assert is_prime(1) is False


def test_get_greeting_with_name():
    result = get_greeting("Олег")
    assert result == "Привіт, Олег!"


def test_get_greeting_empty():
    result = get_greeting("")
    assert result == "Привіт, Анонім!"
