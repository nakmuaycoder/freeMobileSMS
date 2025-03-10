"""

Send a message to free mobile user.

python free_mobile_sms_warning \
    --user=user_id \
    --password=user_pwd
    --message="This is a message"

"""
import argparse
from free_texter import FreeMobileTxtMe


def main() -> None:
    """
    Send a message via sms.

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--user",
                        type=str,
                        required=True,
                        help="Free mobile user"
                        )
    parser.add_argument("--password",
                        type=str,
                        required=True,
                        help="Free mobile password"
                        )
    parser.add_argument("--message",
                        type=str,
                        required=False,
                        default="This is a test message",
                        help="Message to send"
                        )

    args = parser.parse_args()
    warn = FreeMobileTxtMe(free_mobile_user=args.user, free_mobile_pass=args.password)
    warn.send_message(message=args.message)


if __name__ == "__main__":
    main()
