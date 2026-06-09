import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("05 июня 2026", "05 июня 2026"),
    ("123", "123"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("None", "None"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("  ", ""),
    ("  python", "python"),
    ("   python", "python"),
    ("    homework", "homework"),
    ("     windows", "windows"),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("skypro", "skypro"),
    ("", ""),
    ("05 июня 2026", "05 июня 2026"),
    ("None", "None"),
    ("12345", "12345"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("str1, str2, result", [
    ("Skypro", "o", True),
    ("Skypro", "ro", True),
    ("Skypro", "pro", True),
    ("Skypro", "S", True),
    ("Skypro", "r", True),
    ("Skypro", "k", True),
])
def test_strib_positive(str1, str2, result):
    strringUtils = StringUtils()
    res = strringUtils.contains(str1, str2)
    assert res == result


@pytest.mark.negative
@pytest.mark.parametrize("str1, str2, result", [
    ("Skypro", "a", False),
    ("Skypro", "ra", False),
    ("Skypro", "Str", False),
    ("Skypro", "D", False),
    ("Skypro", "T", False),
    ("Skypro", "z", False),
])
def test_strib_negative(str1, str2, result):
    strringUtils = StringUtils()
    res = strringUtils.contains(str1, str2)
    assert res == result


@pytest.mark.positive
@pytest.mark.parametrize("text, symbol, output", [
    ("Text", "T", "ext"),
    ("Text", "t", "Tex"),
    ("12345", "3", "1245"),
    ("12345", "34", "125"),
])
def test_delete_symbol_positive(text, symbol, output):
    my_text = StringUtils()
    assert my_text.delete_symbol(text, symbol) == output


@pytest.mark.positive
@pytest.mark.parametrize("text, symbol, output", [
    ("Text", "f", "Text"),
    ("Text", "K", "Text"),
    ("12345", "0", "12345"),
    ("12345", "87", "12345"),
    ("", "a", ""),
    ("  ", "b", "  "),
])
def test_delete_symbol_negative(text, symbol, output):
    my_text = StringUtils()
    assert my_text.delete_symbol(text, symbol) == output
