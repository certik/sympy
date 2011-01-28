from sympy import var, sqrt, exp, simplify, S, integrate, oo, Symbol, symbols
from sympy.physics.oscillator import E_n, END, spectrum
from sympy.utilities.pytest import raises

var("omega")

def test_oscillator_energies_1D():
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

def test_oscillator_energies_2D():
    n1, n2 = symbols("n1 n2")
    assert END((n1, n2), omega).expand() == \
            (omega * (n1 + n2 + 1)).expand()

    assert END((0, 0)) == 1

    assert END((1, 0)) == 2
    assert END((0, 1)) == 2

    assert END((2, 0)) == 3
    assert END((0, 2)) == 3
    assert END((1, 1)) == 3

    assert END((3, 0)) == 4
    assert END((0, 3)) == 4
    assert END((2, 1)) == 4
    assert END((1, 2)) == 4

    assert END((4, 0)) == 5
    assert END((0, 4)) == 5
    assert END((3, 1)) == 5
    assert END((1, 3)) == 5
    assert END((2, 2)) == 5

    # ...

    raises(ValueError, "END((-1, 0))")

def test_oscillator_energies_3D():
    n1, n2, n3 = symbols("n1 n2 n3")
    assert END((n1, n2, n3), omega).expand() == \
            (omega * (n1 + n2 + n3 + S(3)/2)).expand()

    assert END((0, 0, 0)) == S(3)/2

    assert END((1, 0, 0)) == S(5)/2
    assert END((0, 1, 0)) == S(5)/2
    assert END((0, 0, 1)) == S(5)/2

    assert END((1, 1, 0)) == S(7)/2
    assert END((1, 0, 1)) == S(7)/2
    assert END((0, 1, 1)) == S(7)/2
    assert END((2, 0, 0)) == S(7)/2
    assert END((0, 2, 0)) == S(7)/2
    assert END((0, 0, 2)) == S(7)/2

    assert END((1, 1, 1)) == S(9)/2
    assert END((3, 0, 0)) == S(9)/2
    assert END((0, 3, 0)) == S(9)/2
    assert END((0, 0, 3)) == S(9)/2
    # ...

    raises(ValueError, "END((-1, 0, 0))")

def test_spectrum_2d():
    energies = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6,
            7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9]
    for n in range(len(energies)):
        assert energies[:n] == spectrum(N=2, n=n)
