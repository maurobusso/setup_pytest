import pytest
from lib.present import *

"""when we wrap an item we get it back when we unwrap"""
def test_wrap_and_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33


"""
test initial value of None
"""
def test_content_none():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."

"""
test content present 
"""
def test_content_has_been_wrapped():
    present = Present()
    present.wrap('something')
    with pytest.raises(Exception) as err:
        present.wrap('something')
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."


"""
test content present and not being swapped with new value
"""
def test_content_has_been_wrapped():
    present = Present()
    present.wrap('something')
    with pytest.raises(Exception) as err:
        present.wrap('something else')
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."