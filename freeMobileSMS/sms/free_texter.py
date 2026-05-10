"""
Class for sending an SMS using Free Mobile API.
"""

import logging

import requests

logger = logging.getLogger(__name__)


class FreeMobileTxtMe:
    """Object for sending a message via Free Mobile."""

    def __init__(self, free_mobile_user: str, free_mobile_pass: str, timeout: int = 10):
        """
        Initialize the FreeMobileTxtMe object.

        Args:
            free_mobile_user: Free mobile service user ID.
            free_mobile_pass: Free mobile service password.
            timeout: Request timeout in seconds. Defaults to 10.
        """
        self._user = free_mobile_user
        self._pass = free_mobile_pass
        self._url = "https://smsapi.free-mobile.fr/sendmsg"
        self._timeout = timeout

    def send_message(self, message: str) -> bool:
        """
        Send a text message to mobile.

        Args:
            message: Text message to send.

        Returns:
            bool: True if the message was successfully sent, False otherwise.
        """
        params = {"user": self._user, "pass": self._pass, "msg": message}

        try:
            response = requests.get(self._url, params=params, timeout=self._timeout)
            response.raise_for_status()
            logger.debug("Message sent successfully")
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send message: {type(e).__name__}")
            return False
