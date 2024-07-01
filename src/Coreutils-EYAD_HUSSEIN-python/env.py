"""Env command implementation in python."""

import os


def env() -> None:
    """Print the environment variables

    Args:
        None

    Returns:
        None
    """
    envs = os.environ
    for key, value in envs.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    env()
