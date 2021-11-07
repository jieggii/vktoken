import getpass
import json
from operator import xor

import requests

from vktoken import BUILTIN_APPS
from vktoken.app import App
from vktoken.cli.args import get_arg_parser
from vktoken.cli.log import log_error, log_info


def main():
    parser = get_arg_parser()
    args = parser.parse_args()

    if not args.app and not (args.client_id or args.client_secret):
        parser.error("you should use --app or --client-id and --client-secret keys")

    if args.app and (args.client_id or args.client_secret):
        parser.error("you can't use --app and --client-id or --client-secret at once")

    if not args.app and xor(bool(args.client_id), bool(args.client_secret)):
        parser.error("you must use both --client-id and --client-secret keys")

    if args.app:
        app = BUILTIN_APPS[args.app]
    else:
        app = App(client_id=args.client_id, client_secret=args.client_secret)

    if not args.password:
        args.password = getpass.getpass("Password: ")

    try:
        response = requests.get(
            "https://oauth.vk.com/token"
            "?grant_type=password"
            f"&client_id={app.client_id}"
            f"&client_secret={app.client_secret}"
            f"&username={args.login}"
            f"&password={args.password}"
        ).json()
        access_token = response.get("access_token")
        if access_token:
            log_info(access_token)
        else:
            error_description = response.get("error_description")
            if error_description:
                log_error(error_description.lower(), fatal=True)
            else:
                log_error(response.get("error").lower(), fatal=True)

    except requests.exceptions.ConnectionError:
        log_error("unable to send request. Please check your internet connection", fatal=True)

    except json.JSONDecodeError:
        log_error(
            f"invalid response of the server: {response.text.lower()}",  # noqa
            fatal=True,
        )

    except Exception as err:
        log_error(f"unexpected error: {err}", fatal=True)


if __name__ == "__main__":
    main()
