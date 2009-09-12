"""
This module contains utilities for doing calculations in the Quantum Field
Theory.
"""

from sympy import factorial

def double_factorial(n):
    if n < 0:
        raise ValueError("n must be positive (got %d)" % n)
    elif n == 0:
        return 1
    elif n in [1, 2, 3]:
        return n
    else:
        return n*double_factorial(n-2)

def wick(fields):
    """
    fields is a dict of (i -> n) pairs,
    whose meaning is phi(i)^n
    """
    if len(fields) == 1:
        i = fields.keys()[0]
        n = fields[i]
        if n % 2 == 1:
            return {}
        elif n == 0:
            raise ValueError("power should not be 0")
        else:
            return {frozenset(((i, i),)): double_factorial(n-1)}
    elif len(fields) == 2:
        i, j = fields.keys()
        if (fields[i] + fields[j]) % 2 == 1:
            return {}
        else:
            if fields[i] == fields[j] == 1:
                return {frozenset(((i, j),)): 1}
            else:
                import copy
                d = copy.deepcopy(fields)
                n = d[i]*d[j]
                d[i] -= 1
                d[j] -= 1
                if d[i] == 0:
                    del d[i]
                if d[j] == 0:
                    del d[j]
                r = wick(d)
                result = {}
                for k in r:
                    k2 = set(k)
                    k2.add((i, j),)
                    k2 = frozenset(k2)
                    result[k2] = r[k]*n
                if fields[i] == fields[j] == 2:
                    print result
                    return {
                        frozenset(((i, i), (j, j))): 1,
                        frozenset((i, j)): 2,
                        }
                else:
                    return result
