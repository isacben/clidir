from pycli import command_loader

def main() -> int:
    print("loading commands...")
    command_loader.create_command_dict()
    
    return 0

if __name__ == "__main__":
    exit(main())