import os

from typing import List

def parse(args: List[str], command_files: List[str]) -> List[str]:
    
    command_path_arg = ""
    args_start = 0

    for arg_position in range(len(args)):

        path = "./commands/" + '/'.join(args[:arg_position + 1])

        if path + ".py" in command_files:
            command_path_arg = path + '.py'
            args_start = arg_position + 1
            break

        elif any(path in substring for substring in command_files):
            if os.path.exists(path):
                command_path_arg = path
                args_start = arg_position + 1

        else:
            break

    return [command_path_arg] + args[args_start:]