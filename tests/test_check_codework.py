from lib.check_codeword import *

def test_check_codework():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_if_firs_last_letter():
    result2 = check_codeword('herse')
    assert result2 == "Close, but nope."

def test_with_incorrect_word():
    result3 = check_codeword('cavallo')
    assert result3 == "WRONG!"