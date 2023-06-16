
from dataclasses import dataclass, field
from types import ModuleType

from pycli import help

@dataclass
class Invoker():
    args: list[str] = field(default_factory=list)
    command_paths: list[str] = field(default_factory=list)
    modules: list[ModuleType] = field(default_factory=list)


    def prepare_command(self) -> None:
        pass

        #print("prepare command:", self.args[0])
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
