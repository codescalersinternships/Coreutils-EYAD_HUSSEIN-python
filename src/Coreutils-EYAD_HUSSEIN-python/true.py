"""True command implementation in python."""

import sys


def true() -> None:
    """Do nothing, successfully.

    Args:
        None

    Returns:
        None
    """
    sys.exit(0)


if __name__ == "__main__":
    true()
