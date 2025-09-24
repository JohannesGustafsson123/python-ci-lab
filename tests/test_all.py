from palinlib import is_palindrome

def test_palindrome_simple_odd():
    assert is_palindrome("abcba")

def test_palindrome_simple_even():
    assert is_palindrome("abba")

def test_palindrome_simple_odd_negative():
    assert not is_palindrome("abcca")

def test_palindrome_simple_even_negative():
    assert not is_palindrome("abca")

def test_palindrome_simple_longer_odd():
    assert is_palindrome("abcdefghijkjihgfedcba")

def test_palindrome_simple_longer_even():
    assert is_palindrome("abcdefghijjihgfedcba")

def test_palindrome_empty():
    assert is_palindrome("")

def test_palindrome_one_letter():
    assert is_palindrome("")

def test_palindrome_two_letters():
    assert is_palindrome("aa")

def test_palindrome_two_letters_negative():
    assert not is_palindrome("ab")