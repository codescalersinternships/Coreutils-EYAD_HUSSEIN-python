"""Wc command implementation in python."""

import argparse


def wc() -> None:
    """Print newline, word, and byte counts for each file and a total line
    if more than one FILE is specified

    Args:
        None

    Returns:
        None
    """
    parser = argparse.ArgumentParser(
        "wc",
        description="""Print newline, word, and byte counts for each file and a total line if
        more than one FILE is specified""",
    )
    parser.add_argument("files", nargs="+", help="The files to count")
    parser.add_argument("-c", action="store_true", help="Print the byte counts")
    parser.add_argument("-l", action="store_true", help="Print the newline counts")
    parser.add_argument("-w", action="store_true", help="Print the word counts")
    args = parser.parse_args()

    if not (args.l or args.w or args.c):
        args.l = args.w = args.c = True

    total_lines = 0
    total_words = 0
    total_chars = 0

    for file in args.files:
        with open(file, encoding="utf-8") as f:
            lines = f.readlines()
            words = sum(len(line.split()) for line in lines)
            chars = sum(len(line.encode()) for line in lines)

            if args.l:
                print(len(lines), end=" ")
            if args.w:
                print(words, end=" ")
            if args.c:
                print(chars, end=" ")
            print(file)

            total_lines += len(lines)
            total_words += words
            total_chars += chars

    if len(args.files) > 1:
        if args.l:
            print(total_lines, end=" ")
        if args.w:
            print(total_words, end=" ")
        if args.c:
            print(total_chars, end=" ")
        print("total")


if __name__ == "__main__":
    wc()
