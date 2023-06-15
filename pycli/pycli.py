from pycli import parser
from pycli import command_loader
from pycli.invoker import Invoker

def run(args: list[str]) -> None:

    command_paths = command_loader.commands_lookup()
    parsed_args = parser.parse(args, command_paths)
    print(parsed_args)

    invoker = Invoker(parsed_args, command_paths)
    invoker.prepare_command()