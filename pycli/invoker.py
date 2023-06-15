import importlib
from dataclasses import dataclass
from types import ModuleType

from pycli import help


class Invoker():
    modules: list[ModuleType] = []

    def __init__(self, args: list[str], command_paths: list[str]) -> None:
        self.args = args
        self.command_paths = command_paths


    def load_modules(self) -> None:
        for path in self.command_paths:
            module_string = path.split('./')[1].replace('/', '.').replace('.py', '')
            self.modules.append(importlib.import_module(module_string))
        
        for m in self.modules:
            print(m.__name__, m.description)


    def prepare_command(self) -> None:
        self.load_modules()

        # print("prepare command:", self.args[0])
        # if self.args[0] == '': 
        #     help.print_list_of_commands('')
        #     return
        
        # if 'py' in self.args[0]:
        #     module_string = "commands." + self.args[0].split('.')[0].replace('/', '.')
            
        #     module = importlib.import_module(module_string)
        #     #self.execute(module.Command())

        # else:
        #     print("This should be a directory")
        #     help.print_list_of_commands(self.args[0])

    
    # def execute(self, cmd: BaseCommand):
    #     print(cmd.__class__)
    #     cmd.run(self.args[1:])
