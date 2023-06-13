import argparse
import sys

    
description = "Create a payment"

def run(self):
    parser = argparse.ArgumentParser(
        description='Create a payment')
        
    # NOT prefixing the argument with -- means it's not optional
    parser.add_argument('amount', help="payment amount")
    args = parser.parse_args(sys.argv[3:])
    print(f'Creating a payment for ${args.amount}')