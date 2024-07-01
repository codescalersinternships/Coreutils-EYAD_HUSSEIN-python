import argparse


def yes() -> None:
    parser = argparse.ArgumentParser(
        "yes",
        description="Repeatedly print a line with all specified STRING(s), or 'y'.",
    )
    parser.add_argument("strings", nargs="*", help="The strings to be printed")
    args = parser.parse_args()

    if args.strings:
        while True:
            print(" ".join(args.strings))
    else:
        while True:
            print("y")


if __name__ == "__main__":
    yes()
