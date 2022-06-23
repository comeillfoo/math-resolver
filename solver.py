#!/usr/bin/python
import sys
from utils.preamble import print_preamble
from utils.tex import *
from utils.tasks import *


def main(variant):
    # print preamble of the LaTeX document
    print_preamble()
    with TexEnvironment(None, 'document') as document: # open document environment
        with TexCommand(document, 'section', 'Задание для самостоятельной работы') as section:
            pass

        with EnumerateEnvironment(document) as enumerate:
            enumerate.new_item('Записать первые 3 члена ряда:')
            with series_1_10_first3(enumerate, N=variant) as align:
                pass

            enumerate.new_item('Записать сумму в свернутом виде с общим членом ряда:')


if __name__ == '__main__':
    N = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    main(N)
