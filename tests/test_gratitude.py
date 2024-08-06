import pytest
from lib.gratitudes import *

"""test starting list"""

def test_initial_empty_list():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

"""test adding str"""
def test_add_method():
    gratitude = Gratitudes()
    gratitude.add('food')
    gratitude.add('health')
    assert gratitude.format() == "Be grateful for: food, health"

