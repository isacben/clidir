import argparse
import sys
    
description = 'Retrieve a payment'

def run(self):
    parser = argparse.ArgumentParser(
        description='Retrieve a payment')
        
    # NOT prefixing the argument with -- means it's not optional
    parser.add_argument('token', help="payment token")
    args = parser.parse_args(sys.argv[3:4])
    print('Retrieving the payment', args.token)