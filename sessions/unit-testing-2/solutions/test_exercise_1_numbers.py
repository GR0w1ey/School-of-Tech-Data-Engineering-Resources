from exercise_1_numbers import add_two_numbers, add_number_with_random_number, add_two_random_numbers, get_random_number_di

def test_adds_two_whole_numbers():
    # Arrange
    expected = 2

    # Act
    actual = add_two_numbers(1, 1)

    # Assert
    assert expected == actual

def mock_get_random_number():
    return 5

def test_add_number_with_random_number():
    # Arrange
    a = 5
    expected = 10

    # Act
    actual = add_number_with_random_number(a, mock_get_random_number)

    # Assert
    assert expected == actual

def test_add_two_random_numbers():
    # Arrange
    expected = 10

    # Act
    actual = add_two_random_numbers(mock_get_random_number)

    # Assert
    assert expected == actual

def mock_randint(a, b):
    return 5

def test_get_random_number_randint():
    # Arrange
    expected = 5

    # Act
    actual = get_random_number_di(mock_randint)

    # Assert
    assert expected == actual
