from sys import stdout


default_preamble = """
\\documentclass[10pt, final]{article}

\\usepackage[T2A]{fontenc}
\\usepackage[utf8x]{inputenc}

\\usepackage[english, russian]{babel}

\\usepackage{indentfirst}
\\usepackage{textcomp}
\\usepackage{amsmath, amssymb}
\\usepackage{multirow}
\\usepackage{float}
\\usepackage{subfigure}
\\usepackage{hyperref}

\\usepackage{pdflscape}

\\usepackage{vmargin}
\\setpapersize{A4}
\\setmarginsrb{1cm}{1cm}{1cm}{1cm}{0pt}{0mm}{0pt}{13mm}

\\usepackage{enumitem}
\\makeatletter
\\AddEnumerateCounter{\\asbuk}{\\russian@alph}{щ}
\\makeatother

\\usepackage{graphicx}
\\usepackage{tikz}
\\usetikzlibrary{automata, positioning, arrows}

\\newcommand*\\circled[1]{\\tikz[baseline=(char.base)]{
            \\node[shape=circle,draw,inner sep=2pt] (char) {#1};}}

\\newcommand{\\No}{\\textnumero}
\\newcommand{\\set}[1]{\\{\\,#1\\,\\}}
\\newcommand{\\epsclosure}[1]{\\varepsilon\\_closure(#1)}
\\newcommand{\\moveTo}[2]{moveTo(\\,#1,\\ #2\\,)}

\\sloppy
"""

def print_preamble(file=stdout):
    print(default_preamble, file=file)
