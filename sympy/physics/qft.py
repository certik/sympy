"""
This module contains utilities for doing calculations in the Quantum Field
Theory.
"""

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
            return {frozenset((1, 1)): n // 2}
    elif len(fields) == 2:
        i, j = fields.keys()
        if (fields[i] + fields[j]) % 2 == 1:
            return {}
        else:
            if fields[i] == fields[j] == 1:
                return {frozenset((i, j)): 1}
            else:
                if fields[i] == 1 or fields[j] == 1:
                    return {frozenset((1, 2)): 3}
                else:
                    return {
                        frozenset(((1, 1), (2, 2))): 1,
                        frozenset((1, 2)): 2,
                        }
