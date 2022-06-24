from sys import stdout
from math import exp, sqrt
from .tex import AlignStarEnvironment, EnumerateEnvironment

def series_1_10(N=1):
    return lambda n: (((N + 1) * n - 1) / (2 * n + N))**n

# \sum_{n=1}^\infty &\left(\frac{5n-1}{2n+4}\right)^n\\
def series_1_10_first3(align = AlignStarEnvironment(), N=1):
    align.new_mathline('\\sum_{n=1}^\\infty &\\left(\\frac{%dn-1}{2n+%d}\\right)^n' % (N + 1, N))  
    a_n = series_1_10(N)
    for i in range(1, 4):
        align.new_mathline('a_{%d} &= %f' % ( i, a_n(i) ))


def rolled_series_1_10(align = AlignStarEnvironment(), N=1):
    align.new_mathline('\\frac{1}{%d^2} + \\frac{3}{%d^3} + \\frac{5}{%d^4} + \\cdots' % (N, N, N))
    align.new_mathline('\\sum_{n=1}^\\infty \\frac{2n - 1}{%d^{n+1}}' % N)


def test_convergence_with_neccessary_cond_1_10(align = AlignStarEnvironment(), N=1):
    align.new_mathline('\\sum_{n=1}^\\infty\\frac{%dn - 1}{%dn + 2}' % (N, N+1))
    align.new_mathline('\\text{Проверим: }\\lim_{n\\to\\infty} a_n = 0')
    align.new_mathline('\\lim_{n\\to\\infty}\\frac{%d - \\frac{1}{n}}{%d + \\frac{2}{n}} = \\frac{%d}{%d}\\Rightarrow' % (N, N + 1, N, N+1))
    if (N / (N + 1)) == 0:
        align.new_mathline('\\Rightarrow\\text{ряд сходится}')
    else:
        align.new_mathline('\\Rightarrow\\text{ряд не сходится}')


def test_convergence_with_comparison_sign_1_10(align = AlignStarEnvironment(), N=1):
    align.new_mathline('\\sum_{n=1}^\\infty\\frac{%dn + 1}{9n^2 + n - %d}' % (N * N, N))
    align.new_mathline('\\text{Возьмем несходящийся ряд: }\\sum_{n=1}^\\infty\\frac{1}{n}')
    align.new_mathline('\\text{Исследуем разницу между рядами:}')
    align.new_mathline('\\frac{%dn + 1}{9n^2 + n - %d} - \\frac{1}{n} =' % (N * N, N))
    align.new_mathline('= \\frac{%dn^2 + %d}{9n^3 + n^2 - %dn} \\ge 0' % (N * N - 9, N, N))
    align.new_mathline('\\text{при } \\forall n: n \\ge N: N = 1,\\text{первый ряд больше второго} (0 \\leq a_n \\leq b_n)\\Rightarrow')
    align.new_mathline('\\Rightarrow\\text{по признаку сравнения ряд расходится}')


def test_convergence_with_dalamber_1_10(align = AlignStarEnvironment(), N=1):
    align.new_mathline('\\sum_{n=1}^\\infty\\frac{%d\\cdot 2^n}{(3n)!}' % N)
    align.new_mathline('\\lim_{n\\to\\infty}\\left|\\frac{%d\\cdot 2^{n+1}}{(3n+3)!}\\frac{(3n)!}{%d\\cdot 2^n}\\right| =' % (N, N))
    align.new_mathline('= \\lim_{n\\to\\infty}\left|\\frac{2}{(3n + 3)(3n + 2)(3n + 1)}\\right| = 0 < 1\\Rightarrow')
    align.new_mathline('\\Rightarrow\\text{ряд сходится по признаку Даламбера}')


def test_convergence_with_koshi_1_10(align = AlignStarEnvironment(), N=1):
    align.new_mathline('\\sum_{n=1}^\\infty &\\frac{%d}{2^n}\\left(1 + \\frac{1}{n}\\right)^{n^2}' % N)
    align.new_mathline('\\lim_{n\\to\\infty}\\sqrt[n]{\\frac{%d}{2^n}\\left(1 + \\frac{1}{n}\\right)^{n^2}} &=' % N)
    align.new_mathline('&= \\lim_{n\\to\\infty}\\frac{\\sqrt[n]{%d}}{2}\\left(1 + \\frac{1}{n}\\right)^{n} =' % N)
    align.new_mathline('&= \\frac{1}{2}\\lim_{n\\to\\infty}\\left(1 + \\frac{1}{n}\\right)^{n} =')
    limit = exp(1) / 2
    align.new_mathline('&= \\frac{e}{2} \\approx %f > 1\\Rightarrow' % limit)
    align.new_mathline('&\\Rightarrow\\text{ряд расходится}')


def find_set(subtask, U, X, Y, Z):
    t1 = X.intersection(U.difference(Y))
    subtask.new_item('$ X \\cap \\bar Y = \\set{} $'.format(str(t1)))
    t2 = U.difference(X).intersection(U.difference(Y))
    subtask.new_item('$\\bar X \\cap \\bar Y = \\set{} $'.format(str(t2)))
    t3 = U.difference(X.intersection(Y))
    subtask.new_item('$\\overline{X\\cap Y} = \\set%s $' % str(t3))
    t4 = U.difference(X.union(Y))
    subtask.new_item('$\\overline{X\\cup Y} = \\set%s $' % str(t4))
    t5 = X.difference(Z)
    subtask.new_item('$X \\backslash Z = \\set%s $' % str(t5))
    t6 = X.union(Y).union(Z)
    subtask.new_item('$(X \\cup Y)\\cup Z = \\set%s $' % str(t6))
    t7 = X.intersection(Z).union(U.difference(Y))
    subtask.new_item('$(X \\cap Z)\\cup\\bar Y = \\set%s $' % str(t7))
    t8 = X.union(Y.intersection(Z))
    subtask.new_item('$ X\\cup (Y\\cap Z) = \\set%s $' % str(t8))
    t9 = X.union(Y.union(Z))
    subtask.new_item('$ X\\cup (Y\\cup Z) = \\set%s $' % str(t9))
    t0 = X.difference(Z).union(Y.difference(Z))
    subtask.new_item('$ (X \\backslash Z)\\cup (Y\\backslash Z) = \\set%s $' % str(t0))


def common_solution_difeq_1(align = AlignStarEnvironment(), N=1):
    align.new_mathline('\\text{Находим общее решение однородного уравнения:}&')
    align.new_mathline('y\' + %dxy &= 0' % N)
    align.new_mathline('\\int\\frac{dy}{y} &= -%d\\int xdx' % N)
    align.new_mathline('\\ln{|y|} &= -%fx^2 + C_0' % (N / 2))
    align.new_mathline('\\text{Выражаем константу:}&')
    align.new_mathline('y(x) &= C(x)e^{-%.2fx^2}' % (N / 2))
    align.new_mathline('C\'(x)e^{-%.2fx^2} - %.2fxC(x)e^{-%.2fx^2} + %.2fxC(x)e^{-%.2fx^2} &= xe^{-x^2}' % (N / 2, N, N / 2, N, N / 2))
    align.new_mathline('C\'(x)e^{-%.2fx^2} &= xe^{-x^2}' % (N / 2))
    align.new_mathline('C\'(x) &= xe^{%.2fx^2}' % (N / 2 - 1))
    align.new_mathline('\\int dC(x) &= \\int xe^{%.2fx^2}dx' % (N / 2 - 1))
    align.new_mathline('C(x) &= \\frac{e^{%.2fx^2}}{%.2f} + c_0' % (N / 2 - 1, 2 * (N / 2 - 1)))
    align.new_mathline('\\text{Итого:}&')
    align.new_mathline('y(x) &= \\frac{1}{%.2f}e^{-x^2} + c_0e^{-%.2fx^2}' % (2 * (N / 2 - 1), N / 2))


def common_solution_difeq_2(align = AlignStarEnvironment(), N = 1):
    align.new_mathline('y\'x\\ln{x} - \\ln{x} &= %dy' % (N + 1))
    align.new_mathline('y\' - \\frac{1}{x} &= \\frac{%dy}{x\\ln{x}}' % (N + 1))
    align.new_mathline('y\' - \\frac{%dy}{x\\ln{x}} &= \\frac{1}{x}' % (N + 1))
    align.new_mathline('\\text{Находим общее решение однородного уравнения:}&')
    align.new_mathline('y\' - \\frac{%dy}{x\\ln{x}} &= 0' % (N + 1))
    align.new_mathline('\\int\\frac{dy}{%dy} &= \\int\\frac{dx}{x\\ln{x}} + C_0' % (N + 1))
    align.new_mathline('\\frac{1}{%d}\\ln{y} &= \\int\\frac{d(\\ln{x})}{\\ln{x}} + C_0' % (N + 1))
    align.new_mathline('\\frac{1}{%d}\\ln{y} &= \\ln{\\ln{x}} + C_0' % (N + 1))
    align.new_mathline('\\ln{y} &= %d\\ln{\\ln{x}} + C_1' % (N + 1))
    align.new_mathline('y(x) &= C(x)\\ln^{%d}{x}' % (N + 1) )
    align.new_mathline('\\text{Выражаем константу:}&')
    align.new_mathline('xC\'(x)\\ln^{%d}{x} + %dC(x)\\ln^{%d}{x} - \\ln{x} &= %dC(x)\\ln^{%d}{x}' % (N + 2, N + 1, N + 1, N + 1, N + 1))
    align.new_mathline('xC\'(x)\\ln^{%d}{x} &= 1' % (N + 1))
    align.new_mathline('\\int dC(x) &= \\int\\frac{dx}{x\\ln^{%d}{x}}' % (N + 1))
    align.new_mathline('C(x) &= \\int\\frac{d(\\ln{x})}{\\ln^{%d}{x}} + c' % (N + 1))
    align.new_mathline('C(x) &= -\\frac{1}{%d\\ln^{%d}{x}} + c' % (N, N))
    align.new_mathline('\\text{Итого:}&')
    align.new_mathline('y(x) &= -\\frac{1}{%d}\\ln{x} + c\\ln^{%d}{x}' % (N, N + 1))


def common_solution_difeq_3(align = AlignStarEnvironment(), N = 1):
    align.new_mathline('\\text{Находим общее решение однородного уравнения:}&')
    align.new_mathline('y\' + 2y &= 0')
    align.new_mathline('\\int\\frac{dy}{y} &= -2\\int dx')
    align.new_mathline('\\ln{y} &= -2x + C_0')
    align.new_mathline('y(x) &= C(x)e^{-2x}')
    align.new_mathline('\\text{Выражаем константу:}&')
    align.new_mathline('C\'(x)e^{-2x} - 2e^{-2x}C(x) + 2e^{-2x}C(x) &= %dx' % N)
    align.new_mathline('C\'(x)e^{-2x} &= %dx' % N)
    align.new_mathline('\\int dC(x) &= %d\\int xe^{2x}dx + c_0' % N)
    align.new_mathline('C(x) &= %.2fe^{2x}(2x - 1) + c' % (N / 4))
    align.new_mathline('\\text{Итого:}&')
    align.new_mathline('y(x) &= %.2fx - %.2f) + ce^{-2x}' % (N / 2, N / 4))


def partial_solution_difeq_1(align = AlignStarEnvironment(), N = 1):
    align.new_mathline('\\text{Находим общее решение однородного уравнения:}&')
    align.new_mathline('y\' - y\\cot{x} &= 0')
    align.new_mathline('\\int\\frac{dy}{y} &= \\int\\cot{x}dx')
    align.new_mathline('\\ln{y} &= \\ln{\\sin{x}} + C_0')
    align.new_mathline('y(x) &= C(x)\\sin{x}')
    align.new_mathline('\\text{Выражаем константу:}&')
    align.new_mathline('C\'(x)\\sin{x} + C(x)\\cos{x} - C(x)\\cos{x} &= %dx\\sin{x}' % N)
    align.new_mathline('C\'(x) &= %dx' % N)
    align.new_mathline('\\int dC(x) &= %d\\int xdx' % N)
    align.new_mathline('C(x) &= %.2fx^2 + c_0' % (N / 2))
    align.new_mathline('\\text{Итого:}&')
    align.new_mathline('y(x) &= %.2fx^2\\sin{x} + c_0\\sin{x}' % (N / 2))
    align.new_mathline('\\text{Находим частное решение:}&')
    align.new_mathline('y(\\frac{\\pi}{2}) &= 0 = %.2f\\pi^2 + c_0' % (N / 8))
    align.new_mathline('c_0 &= -%.2f\\pi^2' % (N / 8))
    align.new_mathline('y(x) &= %.2fx^2\\sin{x} - %.2f\\pi^2\\sin{x}' % (N / 2, N / 8))


def partial_solution_difeq_2(align = AlignStarEnvironment(), N = 1):
    align.new_mathline('\\text{Находим общее решение однородного уравнения:}&')
    align.new_mathline('y\' &= %dx' % (N - 2))
    align.new_mathline('\\int dy &= %d\\int xdx' % (N - 2))
    align.new_mathline('y &= %.2fx^2 + c_0' % (N / 2 - 1))
    align.new_mathline('\\text{Находим частное решение:}&')
    align.new_mathline('y(1) &= 4 = %.2f + c_0' % (N / 2 - 1))
    align.new_mathline('c_0 &= %.2f' % (5 - N / 2))
    align.new_mathline('y(x) &= %.2fx^2 + %.2f' % (N / 2 - 1, 5 - N / 2))


def common_solution_difeq_4(align = AlignStarEnvironment(), N = 1):
    align.new_mathline('(%d + %dy^2)xdx &= (%dx^2 + %d)ydy' % (N, N - 3, N - 4, N))
    align.new_mathline('\\int\\frac{xdx}{%dx^2 + %d} &= \\int\\frac{ydy}{%d + %dy^2} + c_0' % (N - 4, N, N, N - 3))
    align.new_mathline('\\frac{1}{%d}\\int\\frac{d(%dx^2 + %d)}{%dx^2 + %d} &= \\frac{1}{%d}\\int\\frac{d(%dy^2 + %d)}{%d + %dy^2} + c_0' % (N - 4, N - 4, N, N - 4, N, N - 3, N - 3, N, N, N - 3))
    align.new_mathline('\\frac{1}{%d}\\ln{%dx^2 + %d} &= \\frac{1}{%d}\\ln{%dy^2 + %d} + c_0' % (N - 4, N - 4, N, N - 3, N - 3, N))


def solve_task(_parent=None, _out=stdout, task=1, N=1):
    align = AlignStarEnvironment(_parent, _out=_out)
    if task == 1:
        series_1_10_first3(align, N)
    elif task == 2:
        rolled_series_1_10(align, N)
    elif task == 3:
        test_convergence_with_neccessary_cond_1_10(align, N)
    elif task == 4:
        test_convergence_with_comparison_sign_1_10(align, N)
    elif task == 5:
        test_convergence_with_dalamber_1_10(align, N)
    elif task == 6:
        test_convergence_with_koshi_1_10(align, N)
    elif task == 8:
        common_solution_difeq_1(align, N)
    elif task == 9:
        common_solution_difeq_2(align, N)
    elif task == 10:
        common_solution_difeq_3(align, N)
    elif task == 11:
        partial_solution_difeq_1(align, N)
    elif task == 12:
        partial_solution_difeq_2(align, N)
    elif task == 13:
        common_solution_difeq_4(align, N)

    with align:
        pass
    
