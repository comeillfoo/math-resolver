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
            with solve_task(enumerate, task=1, N=variant) as task1:
                pass

            enumerate.new_item('Записать сумму в свернутом виде с общим членом ряда:')
            with solve_task(enumerate, task=2, N=variant) as task2:
                pass

            JustText(enumerate).content('Исследовать ряд на сходимость используя...')
            enumerate.new_item('...необходимое условие')
            with solve_task(enumerate, task=3, N=variant) as task3:
                pass


if __name__ == '__main__':
    N = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    main(N)
