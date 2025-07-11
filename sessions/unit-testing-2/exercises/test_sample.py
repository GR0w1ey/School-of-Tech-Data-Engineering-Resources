from sample import add_number_and_random
from unittest.mock import Mock

# dummy function
def dummy_random_number_generator():
    return 1


def test_add_number_and_random_will_add_random_number():
    # act
    num1 = 10
    expected = 11

    # arrange
    result = add_number_and_random(num1, dummy_random_number_generator)

    # assert
    assert result == expected, \
        f"Expected {expected} but was {result}"

def test_add_number_and_random_will_add_random_number_with_mock():
    # Arrange
    num1 = 10
    expected 11
    mock_number_generation = Mock()
    mock_number_generation.return_value = 1

    # Act
    result = add_number_and_random(num1, mock-mock_number_generation)

    # Assert
    assert result == expected, \
        f"Expected {expected} "
