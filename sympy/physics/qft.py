"""
This module contains utilities for doing calculations in the Quantum Field
Theory.
"""

from math import sin, cos, pi

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
    i = fields.keys()[0]
    if len(fields) == 1:
        # special case if there is just one field:
        n = fields[i]
        if n % 2 == 1:
            return []
        elif n == 0:
            raise ValueError("power should not be 0")
        else:
            return [{(i, i): n // 2}]

    # otherwise pick one field and contract it with every other field
    # (including itself):
    result = []
    for j in fields.keys():
        d = fields.copy()
        d[i] -= 1
        if d[j] == 0:
            continue
        d[j] -= 1
        if d[i] == 0:
            del d[i]
        if j != i and d[j] == 0:
            del d[j]
        if d == {}:
            r = [{}]
        else:
            r = wick(d)
        for graph in r:
            graph[(i, j)] = graph.get((i, j), 0) + 1
            if not graph in result:
                result.append(graph)
    return result

def graph2nx(graph):
    import networkx as nx
    G = nx.Graph()
    for edge in graph:
        G.add_edge(*edge)
    return G

def is_connected(graph):
    import networkx as nx
    G = graph2nx(graph)
    return len(nx.connected_components(G)) == 1

def filter_connected(graphs):
    return [g for g in graphs if is_connected(g)]

def graph_plot(graph):
    from matplotlib import pyplot
    fig = pyplot.figure()
    ax = fig.gca()

    fields = graph2fields(graph)
    external = [i for i in fields if fields[i] == 1]
    internal = [i for i in fields if fields[i] != 1]
    n = len(external)
    external_x = [cos(2*pi*i/n) for i in range(n)]
    external_y = [sin(2*pi*i/n) for i in range(n)]
    n = len(internal)
    internal_x = [0.5*cos(2*pi*i/n) for i in range(n)]
    internal_y = [0.5*sin(2*pi*i/n) for i in range(n)]
    ax.plot(external_x, external_y, "go")
    ax.plot(internal_x, internal_y, "bo")
    if len(external) == 2:
        ax.set_ylim(ax.get_xlim())
    ax.set_aspect("equal")
    return fig

def graph2fields(graph):
    fields = {}
    for edge in graph:
        for i in edge:
            fields[i] = fields.get(i, 0) + graph[edge]
    return fields
