import os

def create_command_dict() -> None:
    
    commands_dir = "./commands/"


    res = []
    for (commands_dir, dir_names, file_names) in os.walk(commands_dir):
        res.extend(file_names)
        res.extend(dir_names)
    print(res)