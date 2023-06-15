
def parse(args: list[str], command_files: list[str]) -> list[str]:
    
    command_path_arg = ""
    args_start = 0

    for arg_position in range(len(args)):

        path = "./commands/" + '/'.join(args[:arg_position + 1])

        if path + ".py" in command_files:
            command_path_arg = path + '.py'
            args_start = arg_position + 1
            break

        elif any(path in substring for substring in command_files):
            command_path_arg = path
            args_start = arg_position + 1

        else:
            break

    return [command_path_arg] + args[args_start:]