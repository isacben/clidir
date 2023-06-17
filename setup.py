from setuptools import setup

setup(
    name="pycli",
    version="0.1",
    description="A tiny Python library to easily create CLI applications with sub commands",
    author="Isaac Benitez",
    url="https://github.com/isacben/pycli",
    license="MIT License (MIT)",
    py_modules=["pycli", "arg_parser", "command_loader", "help"]
)