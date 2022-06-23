#!/usr/bin/python
from utils.preamble import print_preamble
from utils.tex import TexEnvironment


def main():
    print_preamble()
    with TexEnvironment(None, 'document') as document:
        pass


if __name__ == '__main__':
    main()
