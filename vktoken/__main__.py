import getpass
import json
import sys
import webbrowser
from argparse import ArgumentParser
from operator import xor

import requests

from vktoken import __version__
from vktoken.app import App

BUILTIN_APPS = {
    "android": App(client_id=2274003, client_secret="hHbZxrka2uZ6jB1inYsH"),
    "iphone": App(client_id=3140623, client_secret="VeWdmVclDCtn6ihuP1nt"),
    "ipad": App(client_id=3682744, client_secret="mY6CDUswIVdJLCD3j15n"),
    "windows-phone": App(client_id=3502557, client_secret="PEObAuQi6KloPM4T30DV"),
}
FAILURE_EXIT_CODE = 1


def log_error(message: str) -> None:
    print(f"Error: {message}.", file=sys.stdout)


def create_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(
        description="Tool for getting VK access token.",
        prog="vktoken",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument("login", type=str, help="VK account login (mobile phone or email)")
    parser.add_argument(
        "password",
        type=str,
        help="VK account password (will be prompted safely if not indicated)",
        nargs="?",
    )
    parser.add_argument(
        "--app",
        type=str,
        choices=BUILTIN_APPS.keys(),
        help="builtin app to be used to auth",
        nargs="?",
    )

    app = parser.add_argument_group("app arguments (can't be used if `--app` was used; must be used both at once)")
    app.add_argument("-cid", "--client-id", type=str, nargs="?", help="app client id")
    app.add_argument("-cs", "--client-secret", type=str, nargs="?", help="app client secret")

    return parser


def main() -> None:
    parser = create_argument_parser()
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
        )
    except requests.exceptions.ConnectionError:
        log_error("unable to send HTTP request. Please check your internet connection")
        sys.exit(FAILURE_EXIT_CODE)

    try:
        response_json = response.json()
    except json.JSONDecodeError:
        log_error(f"invalid response of the server ({response.text})")
        sys.exit(FAILURE_EXIT_CODE)

    access_token = response_json.get("access_token")
    if access_token:
        print(access_token)
    else:
        error = response_json["error"]
        error_description = response_json.get("error_description")

        if error == "need_validation":
            uri = response_json["redirect_uri"]
            print(
                "Validation is required. Please visit the following URI using your web browser:\n"
                f"{uri}\n\n"
                "You will be able to copy access token from the URL bar of your web browser "
                "after submitting code you received from the VK."
            )
            webbrowser.open(uri)

        else:
            log_error(f"{error}{f' ({error_description})' if error_description else ''}")
            sys.exit(FAILURE_EXIT_CODE)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Aborted!\n")
        sys.exit()
