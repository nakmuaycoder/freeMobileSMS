from unittest.mock import Mock, patch

import pytest
import requests

from freeMobileSMS.client import FreeMobileTxtMe


@pytest.fixture
def free_texter():
    return FreeMobileTxtMe("test_user", "test_pass")


@patch("freeMobileSMS.client.requests.get")
def test_send_message_success(mock_get, free_texter):
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = free_texter.send_message("Hello, World!")

    assert result is True
    mock_get.assert_called_once_with(
        "https://smsapi.free-mobile.fr/sendmsg?user=test_user&pass=test_pass&msg=Hello%2C%20World%21",
        timeout=10,
    )


@patch("freeMobileSMS.client.requests.get")
def test_send_message_failure(mock_get, free_texter):
    mock_get.side_effect = requests.exceptions.Timeout("Timeout occurred")

    result = free_texter.send_message("Hello, World!")

    assert result is False
    mock_get.assert_called_once()


@patch("freeMobileSMS.client.requests.get")
def test_send_message_custom_timeout(mock_get):
    free_texter = FreeMobileTxtMe("test_user", "test_pass", timeout=30)
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    free_texter.send_message("Hello, World!")

    mock_get.assert_called_once_with(
        "https://smsapi.free-mobile.fr/sendmsg?user=test_user&pass=test_pass&msg=Hello%2C%20World%21",
        timeout=30,
    )
