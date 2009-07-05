from sympy import sin, cos, exp, E
from sympy.abc import x

def test_sin():
    e = sin(x).lseries(x, 0)
    assert next(e) == x
    assert next(e) == -x**3/6
    assert next(e) == x**5/120

def test_cos():
    e = cos(x).lseries(x, 0)
    assert next(e) == 1
    assert next(e) == -x**2/2
    assert next(e) == x**4/24

def test_exp():
    e = exp(x).lseries(x, 0)
    assert next(e) == 1
    assert next(e) == x
    assert next(e) == x**2/2
    assert next(e) == x**3/6

def test_exp2():
    e = exp(cos(x)).lseries(x, 0)
    assert next(e) == E
    assert next(e) == -E*x**2/2
    assert next(e) == E*x**4/6
    assert next(e) == -31*E*x**6/720
