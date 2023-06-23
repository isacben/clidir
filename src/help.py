from types import ModuleType
from typing import List

def commands(app: str, modules: List[ModuleType], path: str) -> None:
    # when no topic is found
    if path == '':
        topic = 'commands'
        print(f'usage: {app} [-h] command',end="\n\n")
    else:
        # produce format for 'topic': topic1.topic2.topic3
        topic = path.split('./commands/')[1].replace('/', '.')
        print(f'usage: {app} {topic.replace(".", " ")} [-h] command',end="\n\n")
    
    print("commands:")

    cmd_pointer = "" # this helps print the help for the first command in a sub topic
    for m in modules:
        if topic in m.__name__:
            module_elements = m.__name__.split('.')
            
            # deal only with the commands inside the target topic
            i = module_elements.index(topic.split('.')[-1]) # the topic is the deepest folder
            cmd_name = module_elements[i + 1]

            if not cmd_pointer == cmd_name:
                print('  {0:20}  {1}'.format(cmd_name, m.description))

            cmd_pointer = cmd_name