from sympy.physics.qft import wick

assert wick({1: 1}) == {}
assert wick({1: 2}) == {frozenset((1, 1)): 1}
assert wick({1: 3}) == {}
assert wick({1: 4}) == {frozenset((1, 1)): 2}
assert wick({1: 5}) == {}
assert wick({1: 6}) == {frozenset((1, 1)): 3}

assert wick({1: 1, 2: 1}) == {frozenset((1, 2)): 1}
assert wick({1: 2, 2: 1}) == {}
assert wick({1: 1, 2: 2}) == {}
assert wick({1: 1, 2: 3}) == {
        frozenset((1, 2)): 3,
            }
assert wick({1: 2, 2: 2}) == {
        frozenset(((1, 1), (2, 2))): 1,
        frozenset((1, 2)): 2,
            }
assert wick({1: 3, 2: 2}) == {}
assert wick({1: 2, 2: 3}) == {}

#assert wick({1: 1, 2: 1, 3: 1}) == {}
#assert wick({1: 1, 2: 1, 3: 1, 4: 1}) == {
#        frozenset(((1, 2), (3, 4))): 1,
#        frozenset(((1, 3), (2, 4))): 1,
#        frozenset(((1, 4), (2, 3))): 1,
#        }
