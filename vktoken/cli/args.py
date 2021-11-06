from argparse import ArgumentParser

from vktoken import BUILTIN_APPS, __version__


def get_arg_parser():
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
        choices=[key for key in BUILTIN_APPS.keys()],
        help="builtin app to be used to auth",
        nargs="?",
    )

    app = parser.add_argument_group(
        "app arguments (can't be used if `--app` was used; must be used both at once)"
    )
    app.add_argument("-cid", "--client-id", type=str, nargs="?", help="app client id")
    app.add_argument(
        "-cs", "--client-secret", type=str, nargs="?", help="app client secret"
    )

    return parser
