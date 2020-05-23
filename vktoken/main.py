import argparse
import getpass
import json
import sys

import pyperclip
import requests

import vktoken

apps = {
    "android": {"client_id": 2274003, "client_secret": "hHbZxrka2uZ6jB1inYsH"},
    "iphone": {"client_id": 3140623, "client_secret": "VeWdmVclDCtn6ihuP1nt"},
    "ipad": {"client_id": 3682744, "client_secret": "mY6CDUswIVdJLCD3j15n"},
    "windows-phone": {"client_id": 3502557, "client_secret": "PEObAuQi6KloPM4T30DV"},
    "desktop": {"client_id": 3697615, "client_secret": "AlVXZFMUqyrnABp8ncuU"},
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="A tool for getting VK access token", prog="vktoken"
    )
    parser.add_argument(
        "-cp", "--copy", action="store_true", help="copy access token to clipboard",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"vktoken {vktoken.__version__}",
    )
    parser.add_argument("login", type=str, help="your login")
    parser.add_argument("password", type=str, help="your password", nargs="?")
    parser.add_argument(
        "app",
        type=str,
        choices=[key for key in apps],
        default="desktop",
        help="preferred app",
        nargs="?",
    )

    return parser.parse_args()


def main():
    arguments = parse_args()
    app = apps[arguments.app]

    if not arguments.password:
        arguments.password = getpass.getpass("Enter your password: ")

    try:
        response = requests.get(
            "https://oauth.vk.com/token"
            "?grant_type=password"
            f"&client_id={app['client_id']}"
            f"&client_secret={app['client_secret']}"
            f"&username={arguments.login}"
            f"&password={arguments.password}"
        ).json()

    except requests.exceptions.ConnectionError:
        print("Unable to send request. Please check your internet connection")
        sys.exit(-1)

    except json.JSONDecodeError:
        print("Invalid response of the server")
        sys.exit(-1)

    access_token = response.get("access_token")

    if access_token:
        print(f"Access token: {access_token}")

        if arguments.copy:
            try:
                pyperclip.copy(access_token)
                print("Access token has been copied to clipboard")

            except pyperclip.PyperclipException as exception:
                print(f"Error: {exception}")

    else:
        error_description = response.get("error_description")

        if error_description:
            print(f"Error: {error_description}")

        else:
            print(f"Error: {response.get('error')}")
