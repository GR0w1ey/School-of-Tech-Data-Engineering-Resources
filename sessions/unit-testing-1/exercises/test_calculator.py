import pytest
from calculator import Calculator


def test_calculator_correct_output():
  # Arrange
  x = 5
  y = 6
  operator = "+"
  expected = 11
  my_calc = Calculator(x, y, operator)

  # Act
  actual = my_calc.calculate()

  # Assert
  assert expected == actual


def test_calculator_non_numeric_args():
  # Arrange
  x = 5
  y = "6"
  operator = "+"
  my_calc = Calculator(x, y, operator)
  expected_message = 'You entered an invalid type'
  
  # Act & Assert
  with pytest.raises(TypeError, match=expected_message):
     my_calc.calculate()


def test_calculator_invalid_operator():
  # Arrange
  x = 5
  y = 6
  operator = "l"
  my_calc = Calculator(x, y, operator)
  expected_message = "That is an incorrect operator."
  
  # Act & Assert
  with pytest.raises(ValueError, match=expected_message):
    my_calc.calculate()


def test_calculator_invalid_input_range():
  # Arrange
  x = -100001
  y =  5
  operator = "+"
  my_calc = Calculator(x, y, operator)
  expected_message = "Number out of range"

  # Act & Assert
  with pytest.raises(ValueError, match=expected_message):
    my_calc.calculate()
