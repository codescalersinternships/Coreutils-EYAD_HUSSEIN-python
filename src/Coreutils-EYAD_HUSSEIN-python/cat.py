"""Cat command implementation in python."""

import argparse


def cat() -> None:
    """Concatenate files and print on the standard output.

    Args:
        None

    Returns:
        None
    """
    parser = argparse.ArgumentParser(
        "cat", description="Concatenate files and print on the standard output"
    )
    parser.add_argument("files", nargs="+", help="The files to be concatenated")
    parser.add_argument(
        "-n", action="store_true", help="Number the output lines, starting at 1"
    )
    args = parser.parse_args()

    line_number: int = 1
    for file in args.files:
        try:
            with open(file, encoding="utf-8") as f:
                for line in f:
                    if args.n:
                        print(f"{line_number} {line}", end="")
                    else:
                        print(line, end="")
                    line_number += 1
        except FileNotFoundError:
            print(f"file '{file}' not found.")
        except PermissionError:
            print(f"permission denied for file'{file}'")
        except IOError as e:
            print(f"{e} error opening file '{file}'")
        except Exception as e:
            print(f"{e} occurred while reading file '{file}'")


if __name__ == "__main__":
    cat()
