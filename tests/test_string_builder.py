from lib.string_builder import *

"""
test for empty string as starting value
"""
def test_string_builder_empty():
    string = StringBuilder()
    assert string.output() == ""
    assert string.size() == 0


"""
test for empty string as starting value
"""
def test_string_builder_size():
    string = StringBuilder()
    assert string.size() == 0


"""
test the add method
"""
def test_string_builder():
    string = StringBuilder()
    string.add('Hello')
    assert string.output() == "Hello"
    assert string.size() == 5

"""
test for multiple words in string 
"""
def test_string_with_space():
    string = StringBuilder()
    string.add('Hello world!')
    assert string.output() == "Hello world!"
    assert string.size() == 12

"""
test adding multiple strings
"""
def test_concatenating_strings():
    string = StringBuilder()
    string.add('Hello world!')
    string.add("Ciao mamma")
    assert string.output() == "Hello world!Ciao mamma"
    assert string.size() == 22