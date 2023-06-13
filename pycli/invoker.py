import importlib

from pycli.command import BaseCommand
from pycli import help


class Invoker():

    def __init__(self, args: list[str]) -> None:
        self.args = args


    def prepare_command(self) -> None:

        print('./commands/' + self.args[0])
        if self.args[0] == '': 
            help.print_list_of_commands('')
            return
        
        if 'py' in self.args[0]:
            module_string = "commands." + self.args[0].split('.')[0].replace('/', '.')
            
            module = importlib.import_module(module_string)
            self.execute(module.Command())

        else:
            print("This should be a directory")
            help.print_list_of_commands(self.args[0])

    
    def execute(self, cmd: BaseCommand):
        print(cmd.__class__)
        cmd.run(self.args[1:])
