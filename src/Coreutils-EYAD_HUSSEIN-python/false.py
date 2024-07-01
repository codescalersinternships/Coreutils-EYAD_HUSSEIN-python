"""False command implementation in python."""

import sys


def false() -> None:
    """Do nothing, unsuccessfully.

    Args:
        None

    Returns:
        None
    """
    sys.exit(1)


if __name__ == "__main__":
    false()
