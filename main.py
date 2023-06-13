
import sys

from pycli import pycli

def main() -> int:

    args = sys.argv[1:]
    pycli.run(args)

    return 0


if __name__ == "__main__":
    exit(main())


# ** Remember
# *   - add a Callable function somewhere to add the commands: https://www.youtube.com/watch?v=8QsqG9Q14B4
# *   - first you would check the folders; then instantiate the command class and finally use the callable to add the command object