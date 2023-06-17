import sys

from pycli import pycli

def main() -> int:

    args = sys.argv[1:]
    pycli.run(args)

    return 0


if __name__ == "__main__":
    exit(main())