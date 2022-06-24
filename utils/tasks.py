from sys import stdout
from .tex import AlignStarEnvironment

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


def test_convergence_with_comparison_sign_1_10(N=1):
    pass


def solve_task(_parent=None, _out=stdout, task=1, N=1):
    align = AlignStarEnvironment(_parent, _out)
    if task == 1:
        series_1_10_first3(align, N)
    elif task == 2:
        rolled_series_1_10(align, N)
    elif task == 3:
        test_convergence_with_neccessary_cond_1_10(align, N)
    
    return align
