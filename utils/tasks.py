from sys import stdout
from .tex import AlignStarEnvironment

def series_1_10(N=1):
    return lambda n: (((N + 1) * n - 1) / (2 * n + N))**n

# \sum_{n=1}^\infty &\left(\frac{5n-1}{2n+4}\right)^n\\
def series_1_10_first3(_parent=None, _out=stdout, N=1):
    align = AlignStarEnvironment(_parent, _out)
    align.new_mathline('\\sum_{n=1}^\\infty &\\left(\\frac{%dn-1}{2n+%d}\\right)^n' % (N + 1, N))  
    a_n = series_1_10(N)
    for i in range(1, 4):
        align.new_mathline('a_{%d} &= %f' % ( i, a_n(i) ))
    return align



