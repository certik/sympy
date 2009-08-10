from sympy import symbols, factor, sin, cos

from sympy.parsing.maxima_wrapper import Maxima, MaximaError, maxima_present

try:
    import pexpect
    disabled = False
except ImportError:
    disabled = True

if not disabled and not maxima_present():
    disabled = True

def raises(ExpectedException, code):
    """
    Tests, that the "code" raises the ExpectedException exception.

    If so, returns True, otherwise False.
    """
    assert isinstance(code, str)
    import sys
    frame = sys._getframe(1)
    loc = frame.f_locals.copy()
    try:
        exec code in frame.f_globals, loc
    except ExpectedException:
        return True
    return False

def test_basic():
    m = Maxima()
    assert m.run_command("x+y;").strip() == "y+x"
    assert m.run_command("x+y+3;").strip() == "y+x+3"
    assert m.run_command("4 = x;").strip() == "4 = x"

def test_error1():
    m = Maxima()
    assert raises(MaximaError, 'm.run_command("4 == x;")')

def test_factor():
    m = Maxima()
    assert m.run_command("factor (2^63-1);").strip() == \
            "7^2*73*127*337*92737*649657"
    n = 2**63-1
    assert m.factor(n) == factor(n)

    x, y, z, w = symbols("x y z w")
    e = (x+y+z+w)**6
    assert m.factor(e.expand()) == e

def test_integrate():
    m = Maxima()
    assert m.run_command("integrate(sin(x)^3, x);").strip() == \
            "cos(x)^3/3-cos(x)"

    x = symbols("x")
    assert m.run_command("integrate(sin(x)^3, x, 0, %pi);").strip() == "4/3"
    assert m.integrate(x**2, x) == x**3/3
    assert m.integrate(sin(x), x, 0, 1) == 1 - cos(1)
