# freeMobileSMS
Python wrapper for Free mobile SMS API


## syno_warnings

### SMS sender

Send an SMS using [free mobile](https://dev.to/steeve/send-text-notification-from-your-synology-nas-with-free-mobile-sms-jic)
from command line by calling [sms application](freeMobileSMS/sms/__main__.py) or python inside python
script using `FreeMobileTxtMe` class from [`sms`](freeMobileSMS/sms/free_texter.py) package.

```shell
# Send SMS using command line
python freeMobileSMS \
    --user=user_id \
    --password=user_pwd
    --message="This is a message"
```

```python
# Send SMS in python script
from freeMobileSMS.sms import FreeMobileTxtMe

user = "user"
password = "pwd"
message = "This is a test"

free = FreeMobileTxtMe(free_mobile_user=user,
                       free_mobile_pass=password
                       )

free.send_message(message=message)
```

### Logging module

```python
import logging
from freeMobileSMS.logging import Logger

free_mobile_user = "free"
free_mobile_password = "pwd"

# Logger instantiation
logger = Logger(log_name="log_name",
                free_mobile_user=free_mobile_user,
                free_mobile_pass=free_mobile_password
                )

# Log a message
logger.log(level=logging.INFO, message="info")
logger.log(level=logging.ERROR, message="error")
logger.log(level=logging.CRITICAL, message="critical")

# Send an SMS
logger.send_sms(message=f"Your log is available @ {logger.path_log}")
```


