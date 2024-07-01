import argparse


def tail():
    parser = argparse.ArgumentParser(
        "tail", description="Print the last n lines of each file to standard output"
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
            lines = f.readlines()
            for line in lines[-args.n :]:
                print(line, end="")


if __name__ == "__main__":
    tail()
