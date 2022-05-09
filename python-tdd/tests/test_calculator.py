import pytest
import calculator.calculator as calculator

"""
The Red-Green-Refactor cycle:

1. Write a test for a feature that fails
2. Write code to make the test pass
3. Refactor the code as needed

Run it with: #python pytest -v

"""


class TestCalulatorAdd(object):
    def test_when_two_numbers_used_no_exception(self):
        calculator.add("1,2")
        assert 1

    def test_when_non_number_used_throw_exception(self):
        with pytest.raises(ValueError):
            calculator.add("1,X")

    def test_when_empty_string_return_zero(self):
        assert calculator.add("") == 0

    def test_when_one_number_used_return_same_number(self):
        assert calculator.add("3") == 3

    def test_when_two_numbers_used_return_sum(self):
        assert calculator.add("3,6") == 3 + 6

    def test_when_any_number_of_numbers_used_return_sum(self):
        assert calculator.add("3,6,15,18,46,33") == 3 + 6 + 15 + 18 + 46 + 33

    def test_when_new_line_is_used_return_sum(self):
        assert calculator.add("3,6\n15") == 3 + 6 + 15

    def test_when_delimiter_is_specified_use_it(self):
        assert calculator.add("//;\n3;6;15") == 3 + 6 + 15

    def test_when_negative_number_is_used_throw_exception(self):
        with pytest.raises(ValueError):
            calculator.add("3,-6,15,18,46,33")

    def test_when_negative_numbers_are_used_throw_exception(self):
        with pytest.raises(ValueError) as excinfo:
            calculator.add("3,-6,15,-18,46,33")
        assert "Negatives not allowed: [-6, -18]" in str(excinfo.value)

    def test_when_delimiter_is_two_characters_long(self):
        assert calculator.add("//,-\n3,-6,-15") == 3 + 6 + 15

    def test_when_delimiter_is_three_characters_long(self):
        assert calculator.add("//,-%\n3,-%6,-%15") == 3 + 6 + 15
