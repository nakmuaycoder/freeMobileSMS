"""

Log for script monitoring.

"""
import os
import datetime
import getpass
from pathlib import Path
import logging
from .sms import FreeMobileTxtMe


class Logger:

    def __init__(self,
                 log_name: str,
                 free_mobile_user: str = None,
                 free_mobile_pass: str = None
                 ):
        """
        Logger class.
        Log infos and send sms.

        :param log_name: name of log file.
        :param free_mobile_user: free mobile user
        :param free_mobile_pass: free mobile password
        """
        self._log = logging.getLogger(__name__)
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        path = os.path.join(Path.home(), "log/")
        os.makedirs(path, exist_ok=True)
        self.path_log = os.path.join(path, f"{now}_{log_name}.log")

        logging.basicConfig(filename=self.path_log,
                            format='%(asctime)s %(user)s: %(message)s',
                            level=logging.INFO
                            )
        if free_mobile_user is None or free_mobile_pass is None:
            self._sms = None
        else:
            self._sms = FreeMobileTxtMe(free_mobile_user=free_mobile_user,
                                        free_mobile_pass=free_mobile_pass
                                        )

    def log(self, message: str, level: int = 10) -> None:
        """
        Log in log file.
        :param message: text message to log.
        :param level: logging level.
        """
        d = {"user": getpass.getuser()}
        self._log.log(level=level, msg=message, extra=d)

    def send_sms(self, message: str) -> None:
        """
        Send an SMS using free mobile.
        :param message: message to send
        """
        if self._sms is not None:
            self._sms.send_message(message=message)
