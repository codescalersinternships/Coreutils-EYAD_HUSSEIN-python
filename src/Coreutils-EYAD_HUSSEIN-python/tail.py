"""Tail command implementation in python."""

import argparse


def tail() -> None:
    """Print the last n lines of each file to standard output

    Args:
        None

    Returns:
        None
    """
    parser = argparse.ArgumentParser(
        "tail", description="Print the last n lines of each file to standard output"
    )
    parser.add_argument("files", nargs="+", help="The files to print")
    parser.add_argument(
        "-n", type=int, help="The number of lines to be printed", default=10
    )
    args = parser.parse_args()

    for file in args.files:
        try:
            with open(file, encoding="utf-8") as f:
                if len(args.files) > 1:
                    print(f"\n==> {file} <==")
                lines = f.readlines()
                for line in lines[-args.n :]:
                    print(line, end="")
        except FileNotFoundError:
            print(f"file '{file}' not found.")
        except PermissionError:
            print(f"permission denied for file '{file}'.")
        except IOError as e:
            print(f"{e} error opening file '{file}'.")
        except Exception as e:
            print(f"{e} occurred while reading file '{file}'.")


if __name__ == "__main__":
    tail()
