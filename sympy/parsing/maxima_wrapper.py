import os
import re

from sympy.parsing.maxima import parse_maxima

def maxima_present():
    """
    Returns True if Maxima is installed on your system.

    >>> maxima_present()
    True       # can also be False, depends if you have Maxima or not

    """
    import pexpect
    try:
        pexpect.spawn('maxima')
        return True
    except pexpect.ExceptionPexpect:
        return False

class MaximaError(Exception):
    pass

class Maxima(object):
    """
    Pexpect wrapper to the Maxima executable.

    Examples:

    >>> from sympy.parsing.maxima_wrapper import Maxima
    >>> m = Maxima()
    >>> m.run_command("factor(8);")
    2^3
    >>> m.run_command("factor(x^2 + 2*x*y + y^2);")
    (y+x)^2

    >>> from sympy import symbols, sin
    >>> x, y = symbols("x y")
    >>> m.factor(x**2 + 2*x*y + y**2)
    (x + y)**2
    >>> m.integrate(sin(x)**2, x)
    x/2 - sin(2*x)/4
    >>> m.integrate(x**2, x, -1, 1)
    2/3

    """

    def __init__(self):
        import pexpect
        self._child = pexpect.spawn('maxima')
        self._input_id = 1
        self._child.expect('\(%%i%d\)' % self._input_id)
        self.run_command("display2d: false$")

    def run_command(self, command):
        """
        Runs the command in maxima and returns a result.

        Example:

        >>> from sympy.parsing.maxima_wrapper import Maxima
        >>> m = Maxima()
        >>> m.run_command("factor(8);")
        2^3
        >>> m.run_command("factor(x^2 + 2*x*y + y^2);")
        (y+x)^2

        Note: don't forget to put ";" at the end of each maxima command.
        """
        self._child.sendline(command)
        self._child.expect('\(%%i%d\)' % self._input_id)
        id = self._child.expect([
            '\(%%i%d\)' % (self._input_id + 1),
            '\(%%i%d\)' % self._input_id,
            ])
        if id == 1:
            raise MaximaError(self._child.before)
        out = re.split('\(%%o%d\)' % self._input_id,
                self._child.before)
        if len(out) == 2:
            input, output = out
        else:
            output = ""
        self._input_id += 1
        return output

    def factor(self, e):
        """
        Factors a sympy expression using Maxima.

        Example:

        >>> from sympy.parsing.maxima_wrapper import Maxima
        >>> from sympy import symbols
        >>> x, y = symbols("x y")
        >>> m = Maxima()
        >>> m.factor(x**2 + 2*x*y + y**2)
        (x + y)**2

        """
        s = str(e).replace("**", "^")
        r = self.run_command("factor(%s);" % s)
        return parse_maxima(r)

    def integrate(self, e, x, a=None, b=None):
        """
        Integrates a sympy expression using Maxima.

        Examples:

        >>> from sympy.parsing.maxima_wrapper import Maxima
        >>> from sympy import Symbol, sin
        >>> x = Symbol("x")
        >>> m = Maxima()
        >>> m.integrate(x**2, x)
        x**3/3
        >>> m.integrate(sin(x)**2, x)
        x/2 - sin(2*x)/4
        >>> m.integrate(x**2, x, -1, 1)
        2/3

        """
        s = str(e).replace("**", "^")
        if a is None or b is None:
            input = "integrate(%s, %s);" % (s, x)
        else:
            input = "integrate(%s, %s, %s, %s);" % (s, x, a, b)
        r = self.run_command(input)
        return parse_maxima(r)
