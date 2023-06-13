import os


def parse(args: list[str]) -> list[str]:
    
    command_path = ""
    args_start = 0

    for arg_position in range(len(args)):

        path = '/'.join(args[:arg_position + 1])

        if os.path.isfile("./commands/" + path + ".py"):
            command_path = path + '.py'
            args_start = arg_position + 1
            break

        elif os.path.isdir("./commands/" + path):
            command_path = path
            args_start = arg_position + 1

        else:
            break

    return [command_path] + args[args_start:]