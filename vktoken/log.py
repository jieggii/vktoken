import sys


def log_error(message: str, *, fatal: bool = False):
    print(f"Error: {message}", file=sys.stderr)
    if fatal:
        sys.exit(-1)


def log_info(message: str):
    print(message, file=sys.stdout)
