import argparse


__version__ = "1.0.0"


class App:
    available_apps = {
        "android": {"client_id": 2274003, "client_secret": "hHbZxrka2uZ6jB1inYsH"},
        "iphone": {"client_id": 3140623, "client_secret": "VeWdmVclDCtn6ihuP1nt"},
        "ipad": {"client_id": 3682744, "client_secret": "mY6CDUswIVdJLCD3j15n"},
        "windowsphone": {"client_id": 3502557, "client_secret": "PEObAuQi6KloPM4T30DV"},
        "desktop": {"client_id": 3697615, "client_secret": "AlVXZFMUqyrnABp8ncuU"},
    }

    def __init__(self, name: str):
        if name not in self.available_apps:
            raise ValueError("invalid name")

        self.client_id = self.available_apps[name]["client_id"]
        self.client_secret = self.available_apps[name]["client_secret"]


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description="Tool for creating VK access token")
        self.add_argument("login", type=str, help="your login")
        self.add_argument("password", type=str, help="your password", nargs="?")
        self.add_argument(
            "app",
            type=str,
            choices=[key for key in App.available_apps],
            default="desktop",
            help="preferred app",
            nargs="?",
        )

        self.add_argument(
            "-cp",
            "--copy",
            action="store_true",
            help="copy access token to clipboard",
        )

        self.add_argument(
            "-v",
            "--version",
            action="version",
            version=f"vktoken version {__version__}",
        )
