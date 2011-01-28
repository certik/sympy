from sympy import factorial, sqrt, exp, S, laguerre_l, Real

def E_n(n, omega=1):
    """
    Returns the energy of the state "n" of 1D harmonic oscillator.

    We use Hartree atomic units.

    Examples::

    >>> from sympy import var
    >>> from sympy.physics.oscillator import E_n
    >>> var("n w")
    (n, w)
    >>> E_n(n, w)
    w*(1/2 + n)
    >>> E_n(0)
    1/2
    >>> E_n(1)
    3/2
    >>> E_n(2)
    5/2
    >>> E_n(0, 2)
    1
    >>> E_n(2, 2)
    5

    """
    n, omega = S(n), S(omega)
    if n.is_integer and (n < 0):
        raise ValueError("'n' must be nonnegative integer")
    return omega * (n + S(1)/2)
