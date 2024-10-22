import pytest
from string_utils import StringUtils
#positive
@pytest.mark.parametrize('string, string_output',
                         [('restaurant', 'Restaurant'), ('tanja', 'Tanja')])
def test_capitilize_positive(string, string_output):
    util = StringUtils()
    assert util.capitilize(string) == string_output

@pytest.mark.parametrize('string, string_output',
                         [('   restaurant', 'restaurant'), ('   tanja', 'tanja')])
def test_trim_positive(string, string_output):
    util = StringUtils()
    assert util.trim(string) == string_output

@pytest.mark.parametrize('string, delimeter, list_output',
                         [('apple,orange,banana', ',', ['apple', 'orange', 'banana']),
                          ('mon*tus*fri', '*', ['mon', 'tus', 'fri'])])
def test_to_list_positive(string, delimeter, list_output):
    util = StringUtils()
    if delimeter is None:
        assert util.to_list(string) == list_output
    else:
        assert util.to_list(string, delimeter) == list_output


@pytest.mark.parametrize('string, symbol, result',
                         [('restaurant', 'r', True), ('tanja', 'j', True)])
def test_contains_positive(string, symbol, result):
    util = StringUtils()
    assert util.contains(string, symbol) == result

@pytest.mark.parametrize('string, symbol, output_string', [
    ("Atest", "A", "test"),
    ("2Mountain", "2", "Mountain"),
    ("Mary-Anne", "-", "MaryAnne"),
])
def test_delete_symbol_positive(string, symbol, output_string):
    util = StringUtils()
    assert util.delete_symbol(string, symbol) == output_string

@pytest.mark.parametrize('string, symbol, output_string', [
    ("My name Tanja", "M", True),
    ("", "", True),
    ("H90Earphones", "H", True),
    ("Anne-Mary", "A", True),
])
def test_starts_with_positive(string, symbol, output_string):
    util = StringUtils()
    assert util.starts_with(string, symbol) == output_string

@pytest.mark.parametrize('string, symbol, result', [
    ("My favourite season is winter", "r", True),
    ("Pride and Prejudice", "e", True),
    ("", "", True),
    ("Mary Snelly...", ".", True),
])
def test_end_with_positive(string, symbol, result):
    util = StringUtils()
    assert util.end_with(string, symbol) == result

@pytest.mark.parametrize('string, result', [
    ("", True),
    (" ", True),
    ("  ", True),
])
def test_is_empty_positive(string, result):
    util = StringUtils()
    assert util.is_empty(string) == result

@pytest.mark.parametrize('lst, joiner, string', [
    (["apple", "banana", "carrote"], ",", "apple,banana,carrote"),
    ([1,2,3,4,5], None, "1, 2, 3, 4, 5"),
    (["a", "b", "c"], "", "abc"),
    (["Tatyana", "Mikurova"], "-", "Tatyana-Mikurova"),
])
def test_list_to_string_positive(lst, joiner, string):
    util = StringUtils()
    if joiner == None:
        assert util.list_to_string(lst) == string
    else:
        assert util.list_to_string(lst, joiner) == string


#negative
@pytest.mark.parametrize('string, string_output',
                         [('Restaurant', 'Restaurant'), ('Mikurova', 'Mikurova'), ('', '')])
def test_capitilize_negative(string, string_output):
    util = StringUtils()
    assert util.capitilize(string) == string_output

@pytest.mark.parametrize('string, string_output',
                         [('           Honor', 'Honor'), ('.   tanja', '.   tanja'),
                          ('', ''), ('0', '0'), ('     ', '')])
def test_trim_negative(string, string_output):
    util = StringUtils()
    assert util.trim(string) == string_output

@pytest.mark.parametrize('string, delimeter, list_output',
                         [("", None, [])
])
def test_to_list_negative(string, delimeter, list_output):
    util = StringUtils()
    assert util.to_list(string, delimeter) == list_output

@pytest.mark.parametrize('string, symbol, result',
                         [('Jane Austin', 'B', False), ('+79251977294', '3', False),
                          ('Moscow:Index-353570', ' ', False)])
def test_contains_negative(string, symbol, result):
    util = StringUtils()
    assert util.contains(string, symbol) == result

@pytest.mark.parametrize('string, symbol, output_string',
                         [("", "", ""),
                          ("", "M", ""),
                          ("My_last_name_is", " ", "My_last_name_is")
])
def test_delete_symbol_negative(string, symbol, output_string):
    util = StringUtils()
    assert util.delete_symbol(string, symbol) == output_string

@pytest.mark.parametrize('string, symbol, output_string',
                         [("time for tea", "T", False),
                          ("", "&", False),
                          ("Test", "t", False)
])
def test_starts_with_negative(string, symbol, output_string):
    util = StringUtils()
    assert util.starts_with(string, symbol) == output_string

@pytest.mark.parametrize('string, symbol, result', [
    ("My favourite season is winter", "M", False),
    ("Pride and Prejudice", "E", False),
    ("", " ", False),
    ("Mary Snelly...", "a", False),
])
def test_end_with_negative(string, symbol, result):
    util = StringUtils()
    assert util.end_with(string, symbol) == result

@pytest.mark.parametrize('string, result', [
    ("*", False),
    (" Empty string", False),
    ("0", False),
])
def test_is_empty_negative(string, result):
    util = StringUtils()
    assert util.is_empty(string) == result

@pytest.mark.parametrize('lst, joiner, string',
                         [([], None, ""),
                          ([], "*", "")
])
def test_list_to_string_negative(lst, joiner, string):
    util = StringUtils()
    if joiner == None:
        assert util.list_to_string(lst) == string
    else:
        assert util.list_to_string(lst, joiner) == string
