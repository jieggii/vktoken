import argparse
import getpass
import json

import requests

from vktoken import __version__
from vktoken.log import log_error, log_info

apps = {
    "android": {"client_id": 2274003, "client_secret": "hHbZxrka2uZ6jB1inYsH"},
    "iphone": {"client_id": 3140623, "client_secret": "VeWdmVclDCtn6ihuP1nt"},
    "ipad": {"client_id": 3682744, "client_secret": "mY6CDUswIVdJLCD3j15n"},
    "windows-phone": {"client_id": 3502557, "client_secret": "PEObAuQi6KloPM4T30DV"},
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Simple tool for getting VK access token", prog="vktoken",
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "login", type=str, help="VK account login (mobile phone or email)"
    )
    parser.add_argument(
        "password",
        type=str,
        help="VK account password (will be prompted safely if not indicated)",
        nargs="?",
    )
    parser.add_argument(
        "--app",
        type=str,
        choices=[key for key in apps.keys()],
        default="android",
        help="app to be used to auth",
        nargs="?",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    app = apps[args.app]
    if not args.password:
        args.password = getpass.getpass("Password: ")

    try:
        response = requests.get(
            "https://oauth.vk.com/token"
            "?grant_type=password"
            f"&client_id={app['client_id']}"
            f"&client_secret={app['client_secret']}"
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
        log_error(
            "unable to send request. Please check your internet connection", fatal=True
        )

    except json.JSONDecodeError:
        log_error(
            f"invalid response of the server: {response.text.lower()}", fatal=True  # noqa
        )

    except Exception as err:
        log_error(f"unexpected error: {err}", fatal=True)


if __name__ == "__main__":
    main()
