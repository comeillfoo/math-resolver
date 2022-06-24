#!/usr/bin/python
import enum
import sys
from utils.preamble import print_preamble
from utils.tex import *
from utils.tasks import *


def main(variant):
    # print preamble of the LaTeX document
    print_preamble()
    with TexEnvironment(None, 'document') as document: # open document environment
        with TexCommand(document, 'section', 'Задание для самостоятельной работы') as section1:
            pass

        with EnumerateEnvironment(document) as enum1:
            enum1.new_item('Записать первые 3 члена ряда:')
            solve_task(enum1, task=1, N=variant)

            enum1.new_item('Записать сумму в свернутом виде с общим членом ряда:')
            solve_task(enum1, task=2, N=variant)

            JustText(enum1).content('Исследовать ряд на сходимость используя...')
            enum1.new_item('...необходимое условие')
            solve_task(enum1, task=3, N=variant)

            enum1.new_item('...признак сравнения')
            solve_task(enum1, task=4, N=variant)

            enum1.new_item('...признак Даламбера')
            solve_task(enum1, task=5, N=variant)

            enum1.new_item('...признак Коши')
            solve_task(enum1, task=6, N=variant)

        with TexCommand(document, 'section', 'Задание для самостоятельной работы') as section2:
            pass

        with EnumerateEnvironment(document) as enum2:
            enum2.new_item('Пусть $ U = \\set{%d, %d, %d, %d, %d}, X = \\set{%d, %d}, Y = \\set{%d, %d, %d}, Z = \\set{%d, %d} $. Найти множества:' % 
            (N, 2 * N, N + 3, N - 4, 5 - N, N, 5 - N, N, 2 * N, N - 4, 2 * N, 5 - N))
            U = {N, 2 * N, N + 3, N - 4, 5 - N}
            X = {N, 5 - N}
            Y = {N, 2 * N, N - 4}
            Z = {2 * N, 5 - N}
            with EnumerateEnvironment(enum2, ['label=\\asbuk*)', 'ref=\\asbuk*']) as subtasks7:
                find_set(subtasks7, U, X, Y, Z)


if __name__ == '__main__':
    N = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    main(N)
