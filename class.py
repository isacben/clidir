import argparse
import sys

class Payment(object):
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Payment API Object',
            usage='''rapyd <command> [<args>]''')
    
        parser.add_argument('command', help='what to do to the payment')
        args = parser.parse_args(sys.argv[1:2])
        print(args)

        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        
        getattr(self, args.command)()

    def create(self):
        parser = argparse.ArgumentParser(
            description='Create a payment')
        # NOT prefixing the argument with -- means it's not optional
        parser.add_argument('amount')
        args = parser.parse_args(sys.argv[2:])
        print('Creating a payment for ', args.amount)

if __name__ == '__main__':
    Payment()