"""Module for Sympy containers

    (Sympy objects that store other Sympy objects)

    The containers implemented in this module are subclassed to Basic.
    They are supposed to work seamlessly within the Sympy framework.
"""

from basic import Basic

class Tuple(Basic):
    """
    Wrapper around the builtin tuple object

    The Tuple is a subclass of Basic, so that it works well in the
    Sympy framework.  The wrapped tuple is available as self.args, but
    you can also access elements or slices with [:] syntax.

    >>> from sympy import symbols
    >>> from sympy.core.containers import Tuple
    >>> a, b, c, d = symbols('a b c d')
    >>> Tuple(a, b, c)[1:]
    Tuple(b, c)
    >>> Tuple(a, b, c).subs(a, d)
    Tuple(d, b, c)

    """

    def __getitem__(self,i):
        if isinstance(i,slice):
            indices = i.indices(len(self))
            return Tuple(*[self.args[i] for i in range(*indices)])
        return self.args[i]

    def __len__(self):
        return len(self.args)

    def __contains__(self, item):
        return item in self.args

    def __iter__(self):
        return iter(self.args)

    def __add__(self, other):
        if isinstance(other, Tuple):
            return Tuple(*(self.args + other.args))
        elif isinstance(other, tuple):
            return Tuple(*(self.args + other))
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Tuple):
            return Tuple(*(other.args + self.args))
        elif isinstance(other, tuple):
            return Tuple(*(other + self.args))
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Basic):
            return super(Tuple, self).__eq__(other)
        return self.args == other

    def __ne__(self, other):
        if isinstance(other, Basic):
            return super(Tuple, self).__ne__(other)
        return self.args != other

    def __hash__(self):
        return hash(self.args)


def tuple_wrapper(method):
    """
    Decorator that converts any tuple in the function arguments into a Tuple.

    The motivation for this is to provide simple user interfaces.  The user can
    call a function with regular tuples in the argument, and the wrapper will
    convert them to Tuples before handing them to the function.

    >>> from sympy.core.containers import tuple_wrapper, Tuple
    >>> def f(*args):
    ...    return args
    >>> g = tuple_wrapper(f)

    The decorated function g sees only the Tuple argument:

    >>> g(0, (1, 2), 3)
    (0, Tuple(1, 2), 3)

    """
    def wrap_tuples(*args, **kw_args):
        newargs=[]
        for arg in args:
            if type(arg) is tuple:
                newargs.append(Tuple(*arg))
            else:
                newargs.append(arg)
        return method(*newargs, **kw_args)
    return wrap_tuples

class TableForm(Basic):

    def __init__(self, data, headings=None, alignment="left"):
        """
        Creates a TableForm.

        Parameters:

            data ... 2D data to be put into the table
            headings ... gives the labels for entries in each dimension:
                         None ... no labels in any dimension
                         "automatic" ... gives successive integer labels
                         [[l1, l2, ...], ...] gives labels for each entry in
                             each dimension (can be None for some dimension)
            alignment ... "left", "center", "right" (alignment of the columns)
        """
        # We only support 2D data. Check the consistency:
        self._w = len(data[0])
        self._h = len(data)
        for line in data:
            assert len(line) == self._w
        self._lines = data

        if headings is None:
            self._headings = [None, None]
        elif headings == "automatic":
            self._headings = [range(1, self._h + 1), range(1, self._w + 1)]
        else:
            h1, h2 = headings
            if h1 == "automatic":
                h1 = range(1, self._h + 1)
            if h2 == "automatic":
                h2 = range(1, self._w + 1)
            self._headings = [h1, h2]

        self._alignment = alignment

    def as_str(self):
        column_widths = [0] * self._w
        lines = []
        for line in self._lines:
            new_line = []
            for i in range(self._w):
                # Format the item somehow if needed:
                s = str(line[i])
                w = len(s)
                if w > column_widths[i]:
                    column_widths[i] = w
                new_line.append(s)
            lines.append(new_line)

        # Check heading:
        if self._headings[1]:
            new_line = []
            for i in range(self._w):
                # Format the item somehow if needed:
                s = str(self._headings[1][i])
                w = len(s)
                if w > column_widths[i]:
                    column_widths[i] = w
                new_line.append(s)
            self._headings[1] = new_line

        format_str = ""
        for w in column_widths:
            if self._alignment == "left":
                align = "-"
            elif self._alignment == "right":
                align = ""
            else:
                raise NotImplementedError()
            format_str += "%" + align + str(w) + "s "
        format_str += "\n"

        if self._headings[0]:
            self._headings[0] = [str(x) for x in self._headings[0]]
            heading_width = max([len(x) for x in self._headings[0]])
            format_str = "%" + str(heading_width) + "s | " + format_str

        s = ""
        if self._headings[1]:
            d = self._headings[1]
            if self._headings[0]:
                d = [""] + d
            first_line = format_str % tuple(d)
            s += first_line
            s += "-" * (len(first_line) - 2) + "\n"
        for i, line in enumerate(lines):
            d = line
            if self._headings[0]:
                d = [self._headings[0][i]] + d
            s += format_str % tuple(d)
        return s
