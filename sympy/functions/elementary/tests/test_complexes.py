from sympy import symbols, Symbol, sqrt, oo, re, nan, im, sign, I, E, log, \
        pi, arg, conjugate, expand, exp, sin, cos, Function, global_assumptions, Q, Assume
from sympy.utilities.pytest import XFAIL


def test_re():

    x, y, r = symbols('xyr')

    r = Symbol('r')

    global_assumptions.add(Assume(r, Q.real, True))

    assert re(nan) == nan

    assert re(oo) == oo
    assert re(-oo) == -oo

    assert re(0) == 0

    assert re(1) == 1
    assert re(-1) == -1

    assert re(E) == E
    assert re(-E) == -E

    assert re(x) == re(x)
    assert re(x*I) == -im(x)
    assert re(r*I) == 0
    assert re(r) == r

    assert re(x + y) == re(x + y)
    assert re(x + r) == re(x) + r

    assert re(re(x)) == re(x)

    assert re(2 + I) == 2
    assert re(x + I) == re(x)

    assert re(x + y*I) == re(x) - im(y)
    assert re(x + r*I) == re(x)

    assert re(log(2*I)) == log(2)

    assert re((2+I)**2).expand(complex=True) == 3

    global_assumptions.discard(Assume(r, Q.real, True))

def test_im():

    x, y, r = symbols('xyr')

    global_assumptions.add(Assume(r, Q.real, True))

    assert im(nan) == nan

    assert im(oo*I) == oo
    assert im(-oo*I) == -oo

    assert im(0) == 0

    assert im(1) == 0
    assert im(-1) == 0

    assert im(E*I) == E
    assert im(-E*I) == -E

    assert im(x) == im(x)
    assert im(x*I) == re(x)
    assert im(r*I) == r
    assert im(r) == 0

    assert im(x + y) == im(x + y)
    assert im(x + r) == im(x)
    assert im(x + r*I) == im(x) + r

    assert im(im(x)*I) == im(x)

    assert im(2 + I) == 1
    assert im(x + I) == im(x) + 1

    assert im(x + y*I) == im(x) + re(y)
    assert im(x + r*I) == im(x) + r

    assert im(log(2*I)) == pi/2

    assert im((2+I)**2).expand(complex=True) == 4

    global_assumptions.discard(Assume(r, Q.real, True))

def test_sign():
    assert sign(1.2) == 1
    assert sign(-1.2) == -1
    assert sign(0) == 0
    x = Symbol('x')
    assert sign(x).is_zero == False
    assert sign(2*x) == sign(x)

    p = Symbol('p')
    n = Symbol('n')
    m = Symbol('m')

    global_assumptions.add(Assume(p, Q.positive, True))
    global_assumptions.add(Assume(n, Q.negative, True))
    global_assumptions.add(Assume(m, Q.negative, True))

    assert sign(2*p*x) == sign(x)
    assert sign(n*x) == -sign(x)
    assert sign(n*m*x) == sign(x)
    x = 0
    assert sign(x).is_zero == True

    global_assumptions.discard(Assume(p, Q.positive, True))
    global_assumptions.discard(Assume(n, Q.negative, True))
    global_assumptions.discard(Assume(m, Q.negative, True))

def test_abs():
    x, y = symbols('xy')
    assert abs(0) == 0
    assert abs(1) == 1
    assert abs(-1)== 1
    x = Symbol('x')
    n = Symbol('n')

    global_assumptions.add(Assume(x, Q.real, True))
    global_assumptions.add(Assume(n, Q.integer, True))

    assert x**(2*n) == abs(x)**(2*n)
    assert abs(x).diff(x) == sign(x)

    global_assumptions.discard(Assume(x, Q.real, True))
    global_assumptions.discard(Assume(n, Q.integer, True))

def test_abs_real():
    # test some properties of abs that only apply
    # to real numbers
    x = Symbol('x')
    global_assumptions.add(Assume(x, Q.complex, True))
    assert sqrt(x**2) != abs(x)
    assert abs(x**2) != x**2
    global_assumptions.discard(Assume(x, Q.complex, True))

    x = Symbol('x')
    global_assumptions.add(Assume(x, Q.real, True))
    assert sqrt(x**2) == abs(x)
    assert abs(x**2) == x**2
    global_assumptions.discard(Assume(x, Q.real, True))

def test_abs_properties():
    x = Symbol('x')
    assert abs(x).is_real == True
    assert abs(x).is_positive == None
    assert abs(x).is_nonnegative == True

    w = Symbol('w')
    global_assumptions.add(Assume(w, Q.complex, True))
    global_assumptions.add(Assume(w, Q.nonzero, True))
    assert abs(w).is_real == True
    assert abs(w).is_positive == True
    assert abs(w).is_zero == False
    global_assumptions.discard(Assume(w, Q.complex, True))
    global_assumptions.discard(Assume(w, Q.nonzero, True))

    q = Symbol('q')
    global_assumptions.add(Assume(q, Q.positive, True))
    # FIXME: This assumption should be automagically applied.
    global_assumptions.add(Assume(q, Q.nonzero, True))
    assert abs(q).is_real == True
    assert abs(q).is_positive == True
    assert abs(q).is_zero == False
    global_assumptions.discard(Assume(q, Q.positive, True))
    global_assumptions.discard(Assume(q, Q.nonzero, True))

def test_arg():
    assert arg(0) == nan
    assert arg(1) == 0
    assert arg(-1) == pi
    assert arg(I) == pi/2
    assert arg(-I) == -pi/2
    assert arg(1+I) == pi/4
    assert arg(-1+I) == 3*pi/4
    assert arg(1-I) == -pi/4

    p = Symbol('p')
    global_assumptions.add(Assume(p, Q.positive, True))
    assert arg(p) == 0
    global_assumptions.discard(Assume(p, Q.positive, True))

    n = Symbol('n')
    global_assumptions.add(Assume(n, Q.negative, True))
    assert arg(n) == pi
    global_assumptions.discard(Assume(n, Q.negative, True))

def test_conjugate():
    a = Symbol('a')
    global_assumptions.add(Assume(a, Q.real, True))
    assert conjugate(a) == a
    assert conjugate(I*a) == -I*a
    global_assumptions.discard(Assume(a, Q.real, True))

    x, y = symbols('xy')
    assert conjugate(conjugate(x)) == x
    assert conjugate(x + y) == conjugate(x) + conjugate(y)
    assert conjugate(x - y) == conjugate(x) - conjugate(y)
    assert conjugate(x * y) == conjugate(x) * conjugate(y)
    assert conjugate(x / y) == conjugate(x) / conjugate(y)
    assert conjugate(-x) == -conjugate(x)

def test_issue936():
    x = Symbol('x')
    assert abs(x).expand(trig=True)     == abs(x)
    assert sign(x).expand(trig=True)    == sign(x)
    assert arg(x).expand(trig=True)     == arg(x)

def test_issue1655_derivative_conjugate():
    x = Symbol('x')
    f = Function('f')
    assert (f(x).conjugate()).diff(x) == (f(x).diff(x)).conjugate()

def test_derivatives_issue1658():
    x = Symbol('x')
    f = Function('f')
    assert re(f(x)).diff(x) == re(f(x).diff(x))
    assert im(f(x)).diff(x) == im(f(x).diff(x))

    x = Symbol('x')
    global_assumptions.add(Assume(x, Q.real, True))
    assert abs(f(x)).diff(x).subs(f(x), 1+I*x) == x/sqrt(1 + x**2)
    assert arg(f(x)).diff(x).subs(f(x), 1+I*x**2) == 2*x/(1+x**4)
    global_assumptions.discard(Assume(x, Q.real, True))
