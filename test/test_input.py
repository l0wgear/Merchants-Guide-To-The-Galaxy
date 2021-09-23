import merchants_guide.merchants_guide as m
import pytest
import roman

def test_destructure_input():
    input = "glob is I\nprok is V\n\
        glob glob Silver is 34 Credits\n\
        how many Credits is glob prok Silver ?"
    num_assignment = ["glob is I", "prok is V"]
    credit_assignment = ["glob glob Silver is 34 Credits"]
    queries = ["how many Credits is glob prok Silver ?"]

    result_num, result_credit, result_queries = m.destructure_input(input)
    assert num_assignment == result_num
    assert credit_assignment == result_credit
    assert queries == result_queries

def test_get_roman_values():
    num_assignment = ["glob is I", "prok is V"]
    result = {"glob": "I", "prok": "V"}
    assert m.get_roman_values(num_assignment) == result

def test_convert_str_to_decimal():
    roman_values = {"glob": "I", "proc": "V"}
    assert m.convert_str_to_decimal("glob glob", roman_values) is 2
    assert m.convert_str_to_decimal("glob proc", roman_values) is 4

def test_convert_str_to_decimal_InvalidNumeral():
    roman_values = {"glob": "I", "proc": "V"}
    with pytest.raises(roman.InvalidRomanNumeralError):
        m.convert_str_to_decimal("glob glob glob glob", roman_values)

def test_convert_str_to_decimal_KeyError():
    roman_values = {"glob": "I", "proc": "V"}
    with pytest.raises(KeyError):
        m.convert_str_to_decimal("test", roman_values)

def test_get_credit_values():
    roman_values = {"glob": "I", "proc": "V"}
    credit_assignment = ["glob glob Silver is 34 Credits"]
    assert m.get_credit_values(credit_assignment, roman_values) == {"Silver": 17}

def test_calculate_query_results():
    queries = ["how many Credits is glob prok Silver ?"]
    cv = {"Silver": 17}
    rv = {"glob": "I", "prok": "V"}
    assert m.calculate_query_results(queries, cv, rv) == ["glob prok Silver is 68 Credits"]

