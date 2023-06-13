import os

def create_command_dict() -> None:
    
    commands_dir = "./commands/"


    res = []
    for (file_path, dir_names, file_names) in os.walk(commands_dir):
        if "__pycache__" in dir_names:
            dir_names.remove("__pycache__")
        
        if ".DS_Store" in file_names:
            file_names.remove(".DS_Store")

        if len(file_names) > 0:
            for f in file_names:
                res.append(os.path.join(file_path, f))
        
    
    for r in res:
        print(r)