from pycli import parser
from pycli import command_loader
from pycli import help
from pycli.invoker import Invoker

import importlib
from types import ModuleType

def run(args: list[str]) -> None:

    command_paths: list = command_loader.commands_lookup()
    parsed_args: list = parser.parse(args, command_paths)
    modules: list[ModuleType] = []

    # load all available command modules
    for path in command_paths:
        module_string = path.split('./')[1].replace('/', '.').replace('.py', '')
        modules.append(importlib.import_module(module_string))

    print('parsed args:', parsed_args)

    if parsed_args[0] == '': 
        help.commands(modules, '')
    else:
        help.commands(modules, parsed_args[0])


