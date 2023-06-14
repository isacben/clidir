import os

def commands_lookup() -> None:
    
    commands_dir = "./commands/"


    command_file = []
    
    for (file_path, dir_names, file_names) in os.walk(commands_dir):
        if "__pycache__" in dir_names:
            dir_names.remove("__pycache__")
        
        if ".DS_Store" in file_names:
            file_names.remove(".DS_Store")

        if len(file_names) > 0:
            for f in file_names:
                command_file.append(os.path.join(file_path, f))
        
    
    classes_dict = {}
    counter = 0
    for f in command_file:
        counter += 1
        classes_dict[f] = counter
    
    print(classes_dict)