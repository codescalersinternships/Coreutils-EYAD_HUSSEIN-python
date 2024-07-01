"""Env command implementation in python."""

import os


def env() -> None:
    """Print the environment variables

    Args:
        None

    Returns:
        None
    """
    print(os.environ)
    return 0


if __name__ == "__main__":
    env()
