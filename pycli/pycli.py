from pycli import parser
from pycli.invoker import Invoker

def run(args: str) -> None:

    parsed_args = parser.parse(args)
    print(parsed_args)

    invoker = Invoker(parsed_args)
    invoker.prepare_command()