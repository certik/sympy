from sympy import factorial, sqrt, exp, S, laguerre_l, Real

def E_n(n, omega=1):
    """
    Returns the energy of the state "n" of a 1D harmonic oscillator.

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

def END(n_tuple, omega=1):
    """
    Returns the energy of the state "n" of an N-D harmonic oscillator.

    n_tuple ... tuple of (n1, n2, n3, ...).

    len(n_tuple) determines the space dimension

    We use Hartree atomic units.
    """
    # The N-dimensional harmonic oscillator energy is the sum of N independent
    # one-dimensional harmonic oscillators:
    E = 0
    for n in n_tuple:
        E += E_n(n, omega)
    return E
