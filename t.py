from sympy.physics.qft import wick, double_factorial

assert double_factorial(1) == 1
assert double_factorial(2) == 2
assert double_factorial(3) == 3
assert double_factorial(4) == 4*2
assert double_factorial(5) == 5*3
assert double_factorial(6) == 6*4*2
assert double_factorial(7) == 7*5*3
assert double_factorial(8) == 8*6*4*2

assert wick({1: 1}) == []
assert wick({1: 2}) == [{(1, 1): 1}]
assert wick({1: 3}) == []
assert wick({1: 4}) == [{(1, 1): 2}]
assert wick({1: 5}) == []
assert wick({1: 6}) == [{(1, 1): 3}]

assert wick({1: 1, 2: 1}) == [{(1, 2): 1}]
assert wick({1: 2, 2: 1}) == []
assert wick({1: 1, 2: 2}) == []
assert wick({1: 1, 2: 3}) == [{(1, 2): 1, (2, 2): 1}]
assert wick({1: 3, 2: 1}) == [{(1, 2): 1, (1, 1): 1}]
assert wick({1: 2, 2: 2}) == [{(1, 1): 1, (2, 2): 1}, {(1, 2): 2}]
assert wick({1: 3, 2: 2}) == []
assert wick({1: 2, 2: 3}) == []
assert wick({1: 1, 2: 4}) == []
assert wick({1: 1, 2: 5}) == [{(1, 2): 1, (2, 2): 2}]
assert wick({1: 5, 2: 1}) == [{(1, 2): 1, (1, 1): 2}]
#assert wick({1: 3, 2: 3}) == {
#        frozenset(((1, 1), (2, 2))): 1,
#        frozenset((1, 2)): 2,
#            }

#assert wick({1: 1, 2: 1, 3: 1}) == {}
#assert wick({1: 1, 2: 1, 3: 1, 4: 1}) == {
#        frozenset(((1, 2), (3, 4))): 1,
#        frozenset(((1, 3), (2, 4))): 1,
#        frozenset(((1, 4), (2, 3))): 1,
#        }
