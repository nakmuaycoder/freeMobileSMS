"""
Class for sending an SMS using Free Mobile API.
"""

import logging
import urllib.parse

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

        # Free Mobile API is very strict and expects %20 instead of + for spaces.
        # requests uses + by default for query params, so we build the URL manually.
        encoded_msg = urllib.parse.quote(message)
        url = f"{self._url}?user={self._user}&pass={self._pass}&msg={encoded_msg}"

        try:
            response = requests.get(url, timeout=self._timeout)
            response.raise_for_status()
            logger.debug("Message sent successfully")
            return True
        except requests.exceptions.HTTPError as e:
            logger.error(
                f"Failed to send message: HTTP {e.response.status_code} {e.response.reason}"
            )
            return False
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send message: {type(e).__name__} - {e}")
            return False
