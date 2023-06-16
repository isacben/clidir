from types import ModuleType


def commands(modules: list[ModuleType], path: str) -> None:
    # when no topic is found
    if path == '':
        path = './commands'

    # find the deepest folder
    topic = path.split('/')[-1]

    print(f'usage: rapyd {topic} [-h] command',end="\n\n")
    print("commands:")

    cmd_pointer = "" # this helps print the help for the first command in a sub topic
    for m in modules:
        if topic in m.__name__:
            module_elements = m.__name__.split('.')

            # deal only with the commands inside the target topic
            i = module_elements.index(topic)
            cmd_name = module_elements[i + 1]

            if not cmd_pointer == cmd_name:
                print(f'  {cmd_name}        {m.description}')

            cmd_pointer = cmd_name