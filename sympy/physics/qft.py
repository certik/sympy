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
            return []
        elif n == 0:
            raise ValueError("power should not be 0")
        else:
            return [{(i, i): n // 2}]
    elif len(fields) == 2:
        i, j = fields.keys()
        if (fields[i] + fields[j]) % 2 == 1:
            return []
        else:
            if fields[i] == fields[j] == 1:
                return [{(i, j): 1}]

    i = fields.keys()[0]
    result = []
    for j in fields.keys():
        import copy
        d = copy.deepcopy(fields)
        d[i] -= 1
        if d[j] == 0:
            continue
        d[j] -= 1
        if d[i] == 0:
            del d[i]
        if j != i and d[j] == 0:
            del d[j]
        r = wick(d)
        for graph in r:
            graph[(i, j)] = graph.get((i, j), 0) + 1
            if not graph in result:
                result.append(graph)
    print result
    return result
