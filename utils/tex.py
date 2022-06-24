from sys import stdout


class JustText():
    def __init__(self, _parent, _out = stdout):
        self.indent = 0 if _parent == None else _parent.indent + 1
        self.out = _out


    def content(self, contentText):
        print('  ' * self.indent, end = '', file = self.out)
        print(contentText, file = self.out)   


class TexEnvironment:
    def __init__(self, _parent, _name = "section", _out = stdout):
        self.indent = 0 if _parent == None else _parent.indent + 1
        self.name = _name
        self.out = _out


    def __enter__(self):
        print('  ' * self.indent, end = '', file = self.out)
        print('\\begin{%s' % self.name, end = '', file = self.out)
        print('}', file = self.out )
        return self


    def __exit__(self, type, value, traceback):
        print('  ' * self.indent, end = '', file = self.out)
        print('\\end{%s}' % self.name, file = self.out)


    def content(self, contentText):
        print('  ' * (self.indent + 1), end = '', file = self.out)
        print(contentText, file = self.out)


class TexCommand:
    def __init__(self, _parent, _name = "section", _arg = '', _attr = None, _out = stdout):
        self.indent = 0 if _parent == None else _parent.indent + 1
        self.name = _name
        self.out = _out
        self.arg = _arg
        self.attr = _attr


    def __enter__(self):
        print('  ' * self.indent, end = '', file = self.out)
        print('\\%s{' % self.name, end = '', file = self.out)
        print('%s}' % self.arg, end = '', file = self.out )
        if self.attr:
            print('[', end = '', file = self.out)
            print(', '.join([f'{attr}' for attr in self.attr]))
            print(']', file = self.out)
        
        return self


    def __exit__(self, type, value, traceback):
        print()


class ItemizeEnvironment(TexEnvironment):
    def __init__(self, _parent = None, _out=stdout):
        super().__init__(_parent, 'itemize', _out)


    def new_item(self, contentText):
        print('  ' * (self.indent + 1), end = '')
        print('\\item ', end = '')
        print(contentText)


class EnumerateEnvironment(TexEnvironment):
    def __init__(self, _parent = None, _out=stdout):
        super().__init__(_parent, 'enumerate', _out)


    def new_item(self, contentText):
        print('  ' * (self.indent + 1), end = '')
        print('\\item ', end = '')
        print(contentText)


class AlignStarEnvironment(TexEnvironment):
    def __init__(self, _parent = None, _out=stdout):
        super().__init__(_parent, 'align*', _out)
        self.equations = []


    def new_mathline(self, contentText):
        self.equations.append(contentText)


    def __enter__(self):
        super().__enter__()
        for eq in self.equations:
            print('  ' * (self.indent + 1), end = '', file = self.out)
            print(f'{eq}\\\\')

