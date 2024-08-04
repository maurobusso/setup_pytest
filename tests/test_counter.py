from lib.counter import *


"""
Test initial count is zero
"""
def test_initial_counter_value():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

"""
test adding number correctly
"""
def test_add_values():
    counter = Counter()
    counter.add(10)
    assert counter.report() == "Counted to 10 so far."

"""
add multiple number
"""
def test_counter_add_multiple_values():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    assert counter.report() == "Counted to 8 so far."

"""
test for negative numbers
"""
def test_counter_add_multiple_values_one_negative():
    counter = Counter()
    counter.add(5)
    counter.add(-3)
    assert counter.report() == "Counted to 2 so far."