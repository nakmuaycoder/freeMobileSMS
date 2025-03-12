"""

Class for sending a sms using free mobile

"""
from urllib import parse, request


class FreeMobileTxtMe:

    def __init__(self, free_mobile_user: str, free_mobile_pass: str):
        """
        Object for sending a message

        :param free_mobile_user: free mobile service user
        :param free_mobile_pass: free mobile service password
        """
        self._url = f"https://smsapi.free-mobile.fr/sendmsg?user={free_mobile_user}&pass={free_mobile_pass}&msg="

    def _encode_url(self, message: str) -> str:
        """
        Encode the message and add it to url.

        :param message: message to encode
        :return: url to send.
        """
        return self._url + parse.quote(message)

    def send_message(self, message: str) -> None:
        """
        Encode and send a text message to mobile

        :param message: text message to send
        """
        m = self._encode_url(message=message)

        with request.urlopen(m) as _:
            pass

