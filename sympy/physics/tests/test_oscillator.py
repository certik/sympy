from sympy import var, sqrt, exp, simplify, S, integrate, oo, Symbol
from sympy.physics.oscillator import E_n
from sympy.utilities.pytest import raises

var("omega")

def test_oscillator_energies():
    n = Symbol("n")
    assert E_n(n, omega) == omega * (n + S(1)/2)
    assert E_n(n) == n + S(1)/2

    assert E_n(0) == S(1)/2
    assert E_n(1) == S(3)/2
    assert E_n(2) == S(5)/2
    assert E_n(0, 2) == 1
    assert E_n(1, 2) == 3
    assert E_n(2, 2) == 5

    raises(ValueError, "E_n(-1)")
