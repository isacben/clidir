import os

def print_list_of_commands(directory: str) -> None:
    sections = directory.replace("/", " ")
    print(f'usage: rapyd {sections} [-h] command',end="\n\n")
    print("commands:")

    for path in os.listdir("./commands/" + directory):
        if not (path.startswith(".") or path.startswith("_")):
            print("  " + path.split('.')[0])