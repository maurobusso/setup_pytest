from lib.report_length import *

def test_report_length():
    result = report_length("pairing")
    assert result == "This string was 7 characters long."

    result2 = report_length("ibafbiaqewf")
    assert result2 == "This string was 11 characters long."

    result3 = report_length("")
    assert result3 == "This string was 0 characters long."