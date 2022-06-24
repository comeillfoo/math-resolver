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

        print('  $\\mathbf{N}$ соответствует номеру студента по списку в журнале')

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

        print('  $\\mathbf{N}$ соответствует номеру студента по списку в журнале')

        with EnumerateEnvironment(document) as enum2:
            enum2.new_item('Пусть $ U = \\set{%d, %d, %d, %d, %d}, X = \\set{%d, %d}, Y = \\set{%d, %d, %d}, Z = \\set{%d, %d} $. Найти множества:' % 
            (N, 2 * N, N + 3, N - 4, 5 - N, N, 5 - N, N, 2 * N, N - 4, 2 * N, 5 - N))
            U = {N, 2 * N, N + 3, N - 4, 5 - N}
            X = {N, 5 - N}
            Y = {N, 2 * N, N - 4}
            Z = {2 * N, 5 - N}
            with EnumerateEnvironment(enum2, ['label=\\asbuk*)', 'ref=\\asbuk*']) as subtasks7:
                find_set(subtasks7, U, X, Y, Z)

        # TODO: just rewrite solved rest of the tasks for sets
        with TexCommand(document, 'section', 'Задание для самостоятельной работы') as section3:
            pass

        print('  $\\mathbf{N}$ соответствует номеру студента по списку в журнале')

        with EnumerateEnvironment(document) as subtasks8:
            subtasks8.new_item('Найти общее решение дифференциального уравнения:')
            with EnumerateEnvironment(subtasks8) as subtasks8_1:
                subtasks8_1.new_item('$y\' + %dxy = xe^{-x^2}$' % variant)
                solve_task(subtasks8_1, task=8, N=variant)
                subtasks8_1.new_item('$(xy\' - 1)\\ln{x} = %dy$' % (variant + 1))
                solve_task(subtasks8_1, task=9, N=variant)
                subtasks8_1.new_item('$y\' + 2y = %dx$' % variant)
                solve_task(subtasks8_1, task=10, N=variant)

            subtasks8.new_item('Найти частное решение дифференциального уравнения:')
            with EnumerateEnvironment(subtasks8) as subtasks8_2:
                subtasks8_2.new_item('$ y\' - y\\cdot\\cot{x} = %dx\\cdot\\sin{x}; y\\left(\\frac{\\pi}{2}\\right) = 0 $' % variant)
                solve_task(subtasks8_2, task=11, N=variant)
                subtasks8_2.new_item('$ y\' + 2x = %dx; y(1) = 4 $' % variant)
                solve_task(subtasks8_2, task=12, N=variant)

        with TexCommand(document, 'section', 'Задание для самостоятельной работы') as section4:
            pass
        
        print('  $\\mathbf{N}$ соответствует номеру студента по списку в журнале')

        with EnumerateEnvironment(document) as subtasks9:
            subtasks9.new_item('Найти общее решение дифференциального уравнения:')
            with EnumerateEnvironment(subtasks9) as subtasks9_1:
                subtasks9_1.new_item('$%dxdx - (%d)ydy = %dx^2ydy - (%d)xy^2dx$' % (variant, variant, variant - 4, variant - 3))
                solve_task(subtasks9_1, task=13, N=variant)
                subtasks9_1.new_item('$\\sqrt{%d + y^2}dx - ydy = x^2ydy$' % variant)

                subtasks9_1.new_item('$(xy^{%d} + y^{%d}) + y\'(x^{%d} - yx^{%d}) = 0$' % (variant, variant, variant, variant))

            subtasks9.new_item('Найти частное решение дифференциального уравнения:')
            with EnumerateEnvironment(subtasks9) as subtasks9_2:
                subtasks9_2.new_item('$y\' = %d^{x - y}$ при $x = 2,\\ y = 0$' % (variant + 1))
                subtasks9_2.new_item('$y\'\\cdot \\sin^2{x} = %dy$ при $x = \\frac{\\pi}{4},\\ y = e$' % variant)

if __name__ == '__main__':
    N = 1 if len(sys.argv) < 2 else int(sys.argv[1])
    main(N)
