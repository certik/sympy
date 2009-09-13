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
assert wick({1: 3, 2: 3}) == [{(1, 1): 1, (2, 2): 1, (1, 2): 1}, {(1, 2): 3}]

assert wick({1: 1, 2: 1, 3: 1}) == []
assert wick({1: 1, 2: 1, 3: 1, 4: 1}) == [
        {(1, 2): 1, (3, 4): 1},
        {(1, 3): 1, (2, 4): 1},
        {(1, 4): 1, (2, 3): 1},
        ]
assert {(1, 5): 1, (2, 5): 1, (3, 5): 1, (4, 5): 1} in wick({1: 1, 2: 1, 3: 1, 4: 1, 5: 4})
assert {(1, 5): 1, (2, 5): 1, (3, 6): 1, (4, 6): 1, (5, 6): 2} in \
        wick({1: 1, 2: 1, 3: 1, 4: 1, 5: 4, 6:4})
assert wick({1: 1, 2: 1, 3: 1, 4: 1, 5: 3}) == []
assert {(1, 5): 1, (2, 5): 1, (3, 6): 1, (4, 6): 1, (5, 6): 1} in \
        wick({1: 1, 2: 1, 3: 1, 4: 1, 5: 3, 6:3})
