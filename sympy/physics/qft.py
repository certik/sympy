"""
This module contains utilities for doing calculations in the Quantum Field
Theory.
"""

from sympy import factorial

def double_factorial(n):
    if n in [1, 2, 3]:
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
        else:
            return {frozenset((1, 1)): factorial(n-1)}
    elif len(fields) == 2:
        i, j = fields.keys()
        if (fields[i] + fields[j]) % 2 == 1:
            return {}
        else:
            if fields[i] == fields[j] == 1:
                return {frozenset((i, j)): 1}
            else:
                if fields[i] == 1:
                    if fields[j] == 3:
                        return {frozenset(((i, j), (j, j))): 3}
                    else:
                        return {frozenset(((i, j), (j, j))): 15}
                elif fields[j] == 1:
                    if fields[i] == 3:
                        return {frozenset(((i, j), (i, i))): 3}
                    else:
                        return {frozenset(((i, j), (i, i))): 15}
                elif fields[i] == fields[j] == 2:
                    return {
                        frozenset(((i, i), (j, j))): 1,
                        frozenset((i, j)): 2,
                        }
