
import sys
import os
import importlib
import argparse

def main():
    
    args = sys.argv[0:]
    
    if len(args) == 1:
        print("print generic help")
        return
    
    if len(args) == 2:
        if args[1] == '-h':
            print('print root level help')
        else:
            # print help for the root command
            commandHelp(args[1])

    if len(args) > 2:
        if args[2] == '-h':
            commandHelp(args[1])
        else:
            execute(args)
    

def execute(args):
    command = args[1]
    subcommand = args[2]

    module = importlib.import_module("commands."+command+"."+subcommand)
    #class_ = getattr(module, subcommand)
    #instance = class_()
    #instance.run()
    module.run()

def commandHelp(name):
    
    files = [f for f in os.listdir(f'commands/{name}') if os.path.isfile(os.path.join(f'commands/{name}', f))]

    for file in files:
       module = importlib.import_module("commands." + name + "." + file.rsplit('.')[0])
       #print(file.rsplit('.')[0])
       print(module.description)


if __name__ == "__main__":
    main()
