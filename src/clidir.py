import arg_parser
import command_loader
import help

import importlib
from types import ModuleType
from typing import List

def run(args: List[str]) -> None:

    command_paths: list = command_loader.commands_lookup()
    parsed_args: list = arg_parser.parse(args[1:], command_paths)
    modules: List[ModuleType] = []

    # load all available command modules
    for path in command_paths:
        module_string = path.split('./')[1].replace('/', '.').replace('.py', '')
        modules.append(importlib.import_module(module_string))

    if 'py' in parsed_args[0]:
        # convert directory string into the module name
        cmd = parsed_args[0].split('./')[1].replace('/', '.').split('.py')[0]
        for m in modules:
            if m.__name__ == cmd:
                m.run(parsed_args[1:])

    else:
        help.commands(args[0], modules, parsed_args[0])