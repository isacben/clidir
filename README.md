# clidir

[![PyPI](https://img.shields.io/pypi/v/clidir.svg)](https://pypi.org/project/clidir/)
[![Changelog](https://img.shields.io/github/v/release/isacben/clidir?include_prereleases&label=changelog)](https://github.com/isacben/clidir/releases)
[![Tests](https://github.com/isacben/clidir/workflows/Test/badge.svg)](https://github.com/isacben/clidir/actions?query=workflow%3ATest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/isacben/clidir/blob/master/LICENSE)

Create CLI applications with sub commands easily.

## Description

Even simple CLI applications usually require sub commands. For example, `git` has `git remote add`, where *remote* and *add* are sub commands. Doing this with `argparse` or even with more developer friendly libraries can be challenging.

Keeping the commands source code organized in the project can also be complicated.

clidir helps you easily implement commands and sub commands by organizing your Python files in sub directories, so that you can use `argparse` in the simplest way, without the need of `add_subparsers()`.

For example, to create a `git remote add` command, the project structure would be:

```
├── main.py
├── commands/
│     ├── remote/
│           ├── add.py
```

And the implementation of the `add.py` command would be like this:

```python
import argparse

def run(args: list[str]) -> None:
    parser = argparse.ArgumentParser(prog='git remote add')
    parser.add_argument("name")
    parser.add_argument("url")
    
    # the rest of the implementation
```

## Installation

Install this tool using `pip`:

```
pip install clidir
```

## Examples

* [Hello World](https://github.com/isacben/clidir-hello-world)

## Usage

1. Create a `main.py` file with the following code:

```python
import sys
import clidir

def main() -> int:
    args = sys.argv
    clidir.run(args)
    
    return 0

if __name__ == "__main__":
    exit(main())
```

2. Create a `commands` folder.
3. Within the `commands` folder, create sub folders for your commands. For example:

```
├── commands/
│     ├── remote/
│           ├── add.py
```

4. Implement the command. For example, to implement the `add` command, use this boilerplate:

```python
import argparse

description = "what the command does"

def run(args: list[str]) -> None:
    parser = argparse.ArgumentParser(prog='your-app remote add')

    print('running the add command...')
```

5. Test the execution of the command:

```shell
% python3 main.py remote add      
running the add command...
```