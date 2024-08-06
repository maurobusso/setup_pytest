from lib.greet import *

def test_greet():
    result = greet('mauro')
    assert result == "Hello, mauro!"