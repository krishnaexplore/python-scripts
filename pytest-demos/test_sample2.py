from unittest import mock
from unittest.mock import call
from sample2 import random_sum,silly



@mock.patch("sample2.random.randint")
def test_random_sum(mock_randint):
    mock_randint.side_effect = [3,4]
    assert random_sum() == 7
    mock_randint.assert_has_calls(calls=[call(1,10),call(1,10)])


@mock.patch("sample2.random.randint")
@mock.patch("sample2.time.time")
@mock.patch("sample2.requests.get")
def test_silly(mock_reqests_get,mock_time,mock_randint):
    test_params = {
        "timestamp": 123,
        "number": 5
    }
    mock_time.return_value = test_params['timestamp']
    mock_randint.return_value= test_params['number']
    mock_reqests_get.return_value = mock.Mock(name="mock response",**{"status_code": 200,"json.return_value":{"args":test_params}})

    assert silly() == test_params


