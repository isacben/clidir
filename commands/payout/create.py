import argparse

description = "creates a payout"


def run(self, args: list[str]) -> None:
    parser = argparse.ArgumentParser(prog='rapyd payout create')
    parser.add_argument("amount", help="amount")

    new_args = parser.parse_args(args)

    if args == []:
        parser.print_help()
        return

    print(new_args.name)

    #print(f'Customer cus_{random.random()} created, args: {args}')