import pytest
from maths_example import add_two_numbers, price_updater

def test_add_two_numbers_correct_result():
  # Arrange
  num_1 = 1
  num_2 = 2
  expected = 3

  # Act
  result = add_two_numbers(num_1, num_2)

  # Assert
  assert result == expected, \
    f"Expected '{expected}' but was '{result}'"

# Run the test functions.
test_add_two_numbers_correct_result()
print("Done")

def test_price_updater_correct_price_increase():
  # Arrange
  prices = [100.0]
  increase_rate = 0.2
  expected = [120.0]

  # Act
  actual = price_updater(prices, increase_rate)

  # Assert
  assert expected == actual, \
    f"Expected '{expected}' but got '{actual}'"


def test_exception_for_non_numeric_args():
  # Arrange
  prices = [100.0, 200.0, 300.0]
  increase_rate = "0.2"
  
  # Act & Assert
  with pytest.raises(TypeError):
    price_updater(prices, increase_rate)

def test_exception_for_non_numeric_args():
  # Arrange
  prices = [100.0, 200.0, 300.0]
  increase_rate = -0.1

  # Act & Assert
  with pytest.raises(ValueError):
    price_updater(prices, increase_rate)
