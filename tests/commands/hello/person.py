import argparse

from typing import List

description = "say hello to a person"

def run(args: List[str]) -> None:
    parser = argparse.ArgumentParser(prog='cli hello person')
    parser.add_argument("name", help="name of the person to greet")
    
    params = parser.parse_args(args)

    print('Hello', params.name)