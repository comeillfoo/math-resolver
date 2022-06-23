from sys import stdout


class TexEnvironment:
    def __init__(self, _parent, _name = "section", _out=stdout):
        self.indent = 0 if _parent == None else _parent.indent + 1
        self.name = _name
        self.out = _out


    def __enter__(self):
        print('  ' * self.indent, end='', file=self.out)
        print('\\begin{%s' % self.name, end='', file=self.out)
        print('}', file=self.out )
        return self


    def __exit__(self, type, value, traceback):
        print('  ' * self.indent, end='', file=self.out)
        print('\\end{%s}' % self.name, file=self.out)


    def content(self, contentText):
        print( '  ' * (self.indent + 1), end='' )
        print( contentText )
