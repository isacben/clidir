import argparse

description = "creates a customer"


def run(args: list[str]) -> None:
    parser = argparse.ArgumentParser(prog='rapyd customer create')

    parser.add_argument("amount", help="amount")
    parser.add_argument("street-num", help="street number")
    parser.add_argument("-n", "--name", help="customer name ")
    parser.add_argument("-ph", "--phone", help="phone number")

    new_args = parser.parse_args(args)

    if args == []:
        parser.print_help()
        return

    print(new_args.name)