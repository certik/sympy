from primetest import isprime

def divisors(n):
    """
    Return a list of all positive integer divisors of n.

    >>> divisors(24)
    [1, 2, 3, 4, 6, 8, 12, 24]
    """
    n = abs(n)
    if isprime(n):
        return [1, n]
    s = []
    for i in xrange(1, n+1):
        if n % i == 0:
            s += [i]
    return s
