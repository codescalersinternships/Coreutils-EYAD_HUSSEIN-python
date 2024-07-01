import argparse


def head() -> None:
    parser = argparse.ArgumentParser(
        "head", description="Print the first n lines of each file to standard output"
    )
    parser.add_argument("files", nargs="+", help="The files to print")
    parser.add_argument(
        "-n", type=int, help="The number of lines to be printed", default=10
    )
    args = parser.parse_args()

    for file in args.files:
        with open(file) as f:
            if len(args.files) > 1:
                print(f"\n==> {file} <==")
            for i, line in enumerate(f, start=1):
                if i > args.n:
                    break
                print(line, end="")


if __name__ == "__main__":
    head()
