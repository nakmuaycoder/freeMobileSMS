# freeMobileSMS
Python wrapper for Free mobile SMS API

```
freeMobileSMS
│ freeMobileSMS
│ ├── __init__.py
│ ├── logging.py
│ ├── __main__.py
│ └── sms
│     ├── free_texter.py
│     └── __init__.py
├── LICENSE
├── README.md
└── setup.py
```

## Install

```shell
pip install git+https://github.com/nakmuaycoder/freeMobileSMS.git
```

## freeMobileSMS

### SMS sender

Send an SMS using [free mobile](https://dev.to/steeve/send-text-notification-from-your-synology-nas-with-free-mobile-sms-jic)
from command line by calling [sms application](freeMobileSMS/__main__.py) or python inside python
script using `FreeMobileTxtMe` class from [`sms`](freeMobileSMS/sms/free_texter.py) package.

```shell
sms --user=user_id --password=user_pwd --message="This is a test message"
```

or

```shell
python freeMobileSMS \
    --user=user_id \
    --password=user_pwd \
    --message="This is a test message"
```

```python3
# Send SMS in python script
from freeMobileSMS.sms import FreeMobileTxtMe

user = "user"
password = "pwd"
message = "This is a test message"

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


