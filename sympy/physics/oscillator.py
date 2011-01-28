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

def spectrum(N=3, omega=1, n=10):
    """
    Returns the whole spectrum for N-dim oscillator in atomic units.
    """

    # This is a little brute-force approach, but on the other hand it is very
    # robust:
    l = []
    _n = int(float(n)/N) + 1
    if N == 1:
        for i in range(_n):
            l.append(END((i,), omega))
    elif N == 2:
        for i in range(_n):
            for j in range(_n):
                l.append(END((i, j), omega))
    elif N == 3:
        for i in range(_n):
            for j in range(_n):
                for k in range(_n):
                    l.append(END((i, j, k), omega))
    else:
        raise NotImplementedError()
    l.sort()
    return l[:n]
