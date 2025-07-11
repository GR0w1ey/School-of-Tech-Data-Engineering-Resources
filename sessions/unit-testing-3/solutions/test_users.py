from users import get_user_details
from unittest.mock import patch

@patch('builtins.input')
@patch('builtins.print')
def test_get_user_details(mock_print, mock_input):
    mock_input.side_effect = ['Jane', 25]

    get_user_details()

    mock_print.assert_called_with("Thank you, your name is Jane and your age is 25")
    assert mock_input.call_count == 2
    assert mock_print.call_count == 1
