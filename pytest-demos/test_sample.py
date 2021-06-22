from unittest import mock
from sample import guess_number,get_ip
import pytest

@pytest.mark.parametrize("_input,expected",[
    (3,"You own"),
    (4,"You lost")
])
@mock.patch('sample.roll_dice')
def test_guess_number(mock_roll_dice, _input,expected):
    mock_roll_dice.return_value=3
    assert guess_number(_input) == expected
    mock_roll_dice.assert_called_once()

@mock.patch("sample.requests.get")
def test_get_ip(mock_request_get):
    mock_request_get.return_value = mock.Mock(name="Mock repsonse",**{"status_code":200,"json.return_value":{"origin":"0.0.0.0"}})
    ip = get_ip()
    assert ip == '0.0.0.0'