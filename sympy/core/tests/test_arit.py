from sympy import Symbol, sin, cos, exp, O, sqrt, Rational, Real, re, pi, \
        sympify, sqrt, Add, Mul, Pow, I, log
from sympy.utilities.pytest import XFAIL

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

def test_bug1():
    assert re(x) != x
    x.series(x,0,1)
    assert re(x) != x

a = Symbol("a")
b = Symbol("b", positive=True)
c = Symbol("c")

def test_Symbol():
    e=a*b
    assert e==a*b
    assert a*b*b==a*b**2
    assert a*b*b+c==c+a*b**2
    assert a*b*b-c==-c+a*b**2

def test_arit0():
    p = Rational(5)
    e=a*b
    assert e == a*b
    e=a*b+b*a
    assert e == 2*a*b
    e=a*b+b*a+a*b+p*b*a
    assert e == 8*a*b
    e=a*b+b*a+a*b+p*b*a+a
    assert e == a+8*a*b
    e=a+a
    assert e == 2*a
    e=a+b+a
    assert e == b+2*a
    e=a+b*b+a+b*b
    assert e == 2*a+2*b**2
    e=a+Rational(2)+b*b+a+b*b+p
    assert e == 7+2*a+2*b**2
    e=(a+b*b+a+b*b)*p
    assert e == 5*(2*a+2*b**2)
    e=(a*b*c+c*b*a+b*a*c)*p
    assert e == 15*a*b*c
    e=(a*b*c+c*b*a+b*a*c)*p-Rational(15)*a*b*c
    assert e == Rational(0)
    e = Rational(50)*(a-a)
    assert e == Rational(0)
    e=b*a-b-a*b+b
    assert e == Rational(0)
    e=a*b+c**p
    assert e == a*b+c**5
    e=a/b
    assert e == a*b**(-1)
    e=a*2*2
    assert e == 4*a
    e=2+a*2/2
    assert e == 2+a
    e=2-a-2
    assert e == -a
    e=2*a*2
    assert e == 4*a
    e=2/a/2
    assert e == a**(-1)
    e=2**a**2
    assert e == 2**(a**2)
    e = -(1+a)
    assert e == -1 -a
    e = Rational(1,2)*(1+a)
    assert e == Rational(1,2) + a/2

def test_div():
    e=a/b
    assert e == a*b**(-1)
    e=a/b+c/2
    assert e == a*b**(-1)+Rational(1)/2*c
    e=(1-b)/(b-1)
    assert e == (1+-b)*((-1)+b)**(-1)

def test_pow():
    n1 = Rational(1)
    n2 = Rational(2)
    n5 = Rational(5)
    e=a*a
    assert e == a**2
    e=a*a*a
    assert e == a**3
    e=a*a*a*a**Rational(6)
    assert e == a**9
    e=a*a*a*a**Rational(6)-a**Rational(9)
    assert e == Rational(0)
    e=a**(b-b)
    assert e == Rational(1)
    e=(a-a)**b
    # this is a problematic test (only works if "b" is positive):
    #assert e == Rational(0)
    e=(a+Rational(1)-a)**b
    assert e == Rational(1)

    e=(a+b+c)**n2
    assert e == (a+b+c)**2
    assert e.expand() == 2*b*c+2*a*c+2*a*b+a**2+c**2+b**2

    e=(a+b)**n2
    assert e == (a+b)**2
    assert e.expand() == 2*a*b+a**2+b**2

    e=(a+b)**(n1/n2)
    assert e == (a+b)**(Rational(1)/2)
    assert e.expand() == (a+b)**(Rational(1)/2)

    n=n5**(n1/n2)
    assert n == Rational(5)**(Rational(1)/2)
    e=n*a*b-n*b*a
    assert e == Rational(0)
    e=n*a*b+n*b*a
    assert e == 2*a*b*5**(Rational(1)/2)
    assert e.diff(a) == 2*b*5**(Rational(1)/2)
    assert e.diff(a) == 2*b*5**(Rational(1)/2)
    e=a/b**2
    assert e == a*b**(-2)

    assert sqrt(2*(1+sqrt(2))) == (2*(1+2**(Rational(1,2))))**(Rational(1,2))

    x = Symbol('x')
    y = Symbol('y')

    assert ((x*y)**3).expand() == y**3 * x**3
    assert ((x*y)**-3).expand() == y**-3 * x**-3

    assert (x**5*(3*x)**(3)).expand() == 27 * x**8
    assert (x**5*(-3*x)**(3)).expand() == -27 * x**8
    assert (x**5*(3*x)**(-3)).expand() == Rational(1,27) * x**2
    assert (x**5*(-3*x)**(-3)).expand() == -Rational(1,27) * x**2

    # expand_power_exp
    assert (x**(y**(x+exp(x+y))+z)).expand(deep=False) == x**z*x**(y**(x + exp(x + y)))
    assert (x**(y**(x+exp(x+y))+z)).expand() == x**z*x**(y**x*y**(exp(x)*exp(y)))

    n = Symbol('k', even=False)
    k = Symbol('k', even=True)

    assert (-1)**x == (-1)**x
    assert (-1)**n == (-1)**n
    # some problematic tests (depend on assumptions):
    #assert (-2)**k == 2**k
    #assert (-1)**k == 1

@XFAIL
def test_pow2():
    # XXX These fail - they are maybe discutable,
    # let's see SAGE and similar.
    assert ((-x)**2)**Rational(1,3) == ((-x)**Rational(1,3))**2
    assert (-x)**Rational(2,3) == x**Rational(2,3)
    assert (-x)**Rational(5,7) == -x**Rational(5,7)

def test_pow_issue417():
    assert 4**Rational(1, 4) == 2**Rational(1, 2)

def test_pow3():
    assert 2**(Rational(3)/2) == 2 * 2**Rational(1, 2)
    assert 2**(Rational(3)/2) == sqrt(8)

def test_expand():
    p = Rational(5)
    e = (a+b)*c
    assert e == c*(a+b)
    assert (e.expand()-a*c-b*c) == Rational(0)
    e=(a+b)*(a+b)
    assert e == (a+b)**2
    assert e.expand() == 2*a*b+a**2+b**2
    e=(a+b)*(a+b)**Rational(2)
    assert e == (a+b)**3
    assert e.expand() == 3*b*a**2+3*a*b**2+a**3+b**3
    assert e.expand() == 3*b*a**2+3*a*b**2+a**3+b**3
    e=(a+b)*(a+c)*(b+c)
    assert e == (a+c)*(a+b)*(b+c)
    assert e.expand() == 2*a*b*c+b*a**2+c*a**2+b*c**2+a*c**2+c*b**2+a*b**2
    e=(a+Rational(1))**p
    assert e == (1+a)**5
    assert e.expand() == 1+5*a+10*a**2+10*a**3+5*a**4+a**5
    e=(a+b+c)*(a+c+p)
    assert e == (5+a+c)*(a+b+c)
    assert e.expand() == 5*a+5*b+5*c+2*a*c+b*c+a*b+a**2+c**2
    x=Symbol("x")
    s=exp(x*x)-1
    e=s.series(x,0,3)/x**2
    assert e.expand() ==  1+x**2/2+O(x**4)

    e = (x*(y+z))**(x*(y+z))*(x+y)
    assert e.expand(power_exp=False, power_base=False) == x*(x*y + x*z)**(x*y + x*z) + y*(x*y + x*z)**(x*y + x*z)
    assert e.expand(power_exp=False, power_base=False, deep=False) == x*(x*(y + z))**(x*(y + z)) + y*(x*(y + z))**(x*(y + z))
    e = (x*(y+z))**z
    assert e.expand(power_base=True, mul=True, deep=True) in [x**z*(y + z)**z, (x*y + x*z)**z]

    # Check that this isn't too slow
    x = Symbol('x')
    W = 1
    for i in range(1, 21):
        W = W * (x-i)
    W = W.expand()
    assert W.has(-1672280820*x**15)


def test_power_expand():
    """Test for Pow.expand()"""
    a = Symbol('a')
    b = Symbol('b')
    p = (a+b)**2
    assert p.expand() == a**2 + b**2 + 2*a*b

    p = (1+2*(1+a))**2
    assert p.expand() == 9 + 4*(a**2) + 12*a

def test_real_mul():
    Real(0) * pi * x == Real(0)
    Real(1) * pi * x == pi * x
    len((Real(2) * pi * x).args) == 3

def test_ncmul():
    A = Symbol("A", commutative=False)
    B = Symbol("B", commutative=False)
    C = Symbol("C", commutative=False)
    assert A*B != B*A
    assert A*B*C != C*B*A
    assert A*b*B*3*C == 3*b*A*B*C
    assert A*b*B*3*C != 3*b*B*A*C
    assert A*b*B*3*C == 3*A*B*C*b

    assert A+B == B+A
    assert (A+B)*C != C*(A+B)

    assert C*(A+B)*C != C*C*(A+B)

    assert (C*(A+B)).expand() == C*A+C*B
    assert (C*(A+B)).expand() != A*C+B*C

    assert A*A == A**2
    assert (A+B)*(A+B) == (A+B)**2
    assert ((A+B)**2).expand() == A**2 + A*B + B*A +B**2

    assert A**-1  * A == 1
    assert A/A == 1
    assert A/(A**2) == 1/A

    assert A/(1+A) == A/(1+A)

def test_ncpow():
    x = Symbol('x', commutative=False)
    y = Symbol('y', commutative=False)

    assert (x**2)*(y**2) != (y**2)*(x**2)
    assert (x**-2)*y != y*(x**2)

def test_powerbug():
    x=Symbol("x")
    assert x**1 != (-x)**1
    assert x**2 == (-x)**2
    assert x**3 != (-x)**3
    assert x**4 == (-x)**4
    assert x**5 != (-x)**5
    assert x**6 == (-x)**6

    assert x**128 == (-x)**128
    assert x**129 != (-x)**129

    assert (2*x)**2 == (-2*x)**2

def test_Mul_doesnt_expand_exp():
    x = Symbol('x')
    y = Symbol('y')
    assert exp(x)*exp(y) == exp(x)*exp(y)
    assert 2**x*2**y == 2**x*2**y
    assert x**2*x**3 == x**5
    assert 2**x*3**x == 6**x
    assert x**(y)*x**(2*y) == x**(3*y)
    assert 2**Rational(1,2)*2**Rational(1,2) == 2
    assert 2**x*2**(2*x) == 2**(3*x)
    assert 2**Rational(1,2)*2**Rational(1,4)*5**Rational(3,4) == 10**Rational(3,4)
    assert (x**(-log(5)/log(3))*x)/(x*x**( - log(5)/log(3))) == sympify(1)


@XFAIL
def test_Pow_is_bounded():
    x = Symbol('x', real=True)

    assert (x**2).is_bounded == None

    assert (sin(x)**2).is_bounded == True
    assert (sin(x)**x).is_bounded == None
    assert (sin(x)**exp(x)).is_bounded == None

    # XXX This first one fails
    assert (1/sin(x)).is_bounded == False
    assert (1/exp(x)).is_bounded == False

def test_issue432():
    class MightyNumeric(tuple):
        def __rdiv__(self, other):
            return "something"

        def __rtruediv__(self, other):
            return "something"
    assert sympify(1)/MightyNumeric((1,2)) == "something"

def test_issue432b():
    class Foo:
        def __init__(self):
            self.field = 1.0
        def __mul__(self, other):
            self.field = self.field * other
        def __rmul__(self, other):
            self.field = other * self.field
    f = Foo()
    x = Symbol("x")
    assert f*x == x*f

def test_bug3():
    a = Symbol("a")
    b = Symbol("b", positive=True)
    e = 2*a + b
    f = b + 2*a
    assert e == f

def test_suppressed_evaluation():
    a = Add(1,3,2,evaluate=False)
    b = Mul(1,3,2,evaluate=False)
    c = Pow(3,2,evaluate=False)
    assert a != 6
    assert a.func is Add
    assert a.args == (1,3,2)
    assert b != 6
    assert b.func is Mul
    assert b.args == (1,3,2)
    assert c != 9
    assert c.func is Pow
    assert c.args == (3,2)


def test_Add_as_coeff_terms():
    assert (x+1).as_coeff_terms()   == ( 1, (x+1,) )
    assert (x+2).as_coeff_terms()   == ( 1, (x+2,) )
    assert (x+3).as_coeff_terms()   == ( 1, (x+3,) )

    assert (x-1).as_coeff_terms()   == (-1, (1-x,) )
    assert (x-2).as_coeff_terms()   == (-1, (2-x,) )
    assert (x-3).as_coeff_terms()   == (-1, (3-x,) )

    n = Symbol('n', integer=True)
    assert (n+1).as_coeff_terms()   == ( 1, (n+1,) )
    assert (n+2).as_coeff_terms()   == ( 1, (n+2,) )
    assert (n+3).as_coeff_terms()   == ( 1, (n+3,) )

    assert (n-1).as_coeff_terms()   == (-1, (1-n,) )
    assert (n-2).as_coeff_terms()   == (-1, (2-n,) )
    assert (n-3).as_coeff_terms()   == (-1, (3-n,) )

def test_Pow_as_coeff_terms_doesnt_expand():
    assert exp(x + y).as_coeff_terms() == (1, (exp(x + y),))
    assert exp(x + exp(x + y)) != exp(x + exp(x)*exp(y))

def test_issue974():
    assert -1/(-1-x)    == 1/(1+x)
