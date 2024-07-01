import argparse


def cat() -> None:
    parser = argparse.ArgumentParser(
        "cat", description="Concatenate files and print on the standard output"
    )
    parser.add_argument("files", nargs="+", help="The files to be concatenated")
    parser.add_argument(
        "-n", action="store_true", help="Number the output lines, starting at 1"
    )
    args = parser.parse_args()

    i = 1
    for file in args.files:
        with open(file) as f:
            for line in f:
                if args.n:
                    print(f"{i} {line}", end="")
                else:
                    print(line, end="")
                i += 1


if __name__ == "__main__":
    cat()
