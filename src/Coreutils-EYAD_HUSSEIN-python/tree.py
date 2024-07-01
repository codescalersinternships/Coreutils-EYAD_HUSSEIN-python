"""Tree command implementation in python."""

import argparse
import os


def tree() -> None:
    """Print the directory tree structure

    Args:
        None

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Print the directory tree structure")
    parser.add_argument(
        "-L", type=int, default=-1, help="Descend only level directories deep"
    )
    parser.add_argument(
        "directories", nargs="*", default=["."], help="Directories to list"
    )
    args = parser.parse_args()

    for index, directory in enumerate(args.directories):
        print_directory(directory, 0, args.L)
        if index != len(args.directories) - 1:
            print()


def print_listing(entry, depth, max_depth) -> None:
    """Print the directory listing

    Args:
        entry: The entry to be printed
        depth: The depth of the entry
        max_depth: The maximum depth to be printed

    Returns:
        None
    """
    if max_depth != -1 and depth > max_depth:
        return

    indent = "|   " * depth

    if depth == 0:
        print(entry)
    else:
        entry_name = os.path.basename(entry) or os.path.basename(os.path.dirname(entry))
        print(f"{indent}|-- {entry_name}")


def print_directory(path, depth, max_depth) -> None:
    """Print the first n lines of each file to standard output

    Args:
        path: The path of the directory
        depth: The depth of the directory
        max_depth: The maximum depth to be printed

    Returns:
        None
    """
    if max_depth != -1 and depth > max_depth:
        return

    if depth != 0 and os.path.basename(path).startswith("."):
        return

    try:
        entries = os.listdir(path)
    except OSError as e:
        print(f"Error reading {path}: {e.strerror}")
        return

    print_listing(path, depth, max_depth)

    for entry in entries:
        entry_path = os.path.join(path, entry)
        try:
            if os.path.islink(entry_path):
                full_path = os.readlink(entry_path)
                print_listing(f"{entry} -> {full_path}", depth + 1, max_depth)
            elif os.path.isdir(entry_path):
                print_directory(entry_path, depth + 1, max_depth)
            else:
                print_listing(entry, depth + 1, max_depth)
        except OSError as e:
            print(f"Error reading {entry_path}: {e.strerror}")


if __name__ == "__main__":
    tree()
