"""Echo command implementation in python."""

import argparse


def echo() -> None:
    """Outputs input string to standard output.

    Args:
        None

    Returns:
        None
    """
    parser = argparse.ArgumentParser(
        "echo", description="Prints the given strings to the standard output"
    )
    parser.add_argument("strings", nargs="+", help="The strings to be printed")
    parser.add_argument(
        "-n", action="store_true", help="Do not print the trailing newline character"
    )

    args = parser.parse_args()

    output = " ".join(args.strings)
    if args.n:
        print(output, end="")
    else:
        print(output)


if __name__ == "__main__":
    echo()
