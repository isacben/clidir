import argparse

def main():
    parser = argparse.ArgumentParser(prog='rapyd')
    parser.add_argument("--name", help="customer name ")
    new_args = parser.parse_args()

if __name__ == "__main__":
    main()