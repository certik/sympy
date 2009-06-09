from sympy import var, pprint, Symbol, Add, integrate

var("x y")

def get_poly_unordered(vars, order, coeff_name="a"):
    """
    Returns a general polynomial up to the order 'order'.
    The result is not nicely ordered.

    Example:
    >>> t.get_poly([x, y], 2)
    a0 + a1*y + a3*x + a4*x*y + a2*y**2 + a5*x**2
    >>> t.get_poly([x, y], 2, "b")
    b0 + b1*y + b3*x + b4*x*y + b2*y**2 + b5*x**2
    """
    r = 0
    count = 0
    for i in range(order+1):
        for j in range(order+1):
            if i+j <= order:
                s = Symbol(coeff_name+"%d" % count)
                count += 1
                r += s * vars[0]**i * vars[1]**j
    return r

def get_poly(vars, order, coeff_name="a"):
    """
    Returns a general polynomial up to the order 'order'.
    The result is ordered by the order.

    Example:
    >>> t.get_poly([x, y], 2)
    a0 + a1*x + a2*y + a4*x*y + a3*x**2 + a5*y**2
    >>> t.get_poly([x, y], 2, "b")
    b0 + b1*x + b2*y + b4*x*y + b3*x**2 + b5*y**2
    """
    if order == 0:
        count = 0
        s = Symbol(coeff_name+"%d" % count)
        return s
    else:
        r = get_poly(vars, order - 1, coeff_name)
        if not isinstance(r, Add):
            count = 1
        else:
            count = len(r.args)
        for i in range(order+1):
            s = Symbol(coeff_name+"%d" % count)
            count += 1
            r += s * vars[0]**(order-i) * vars[1]**i
        return r

def integrate_line(e, p1, p2):
    """
    Integrates any expression (like a polynomial) over the line p1-p2.
    """
    if p1[0] == p2[0]:
        # vertical line:
        return integrate(e.subs(x, p1[0]), (y, p1[1], p2[1]))
    elif p1[1] == p2[1]:
        # horizontal line:
        return integrate(e.subs(y, p1[1]), (x, p1[0], p2[0]))
    else:
        raise NotImplementedError()

B_x = get_poly([x, y], 3, "a")
B_y = get_poly([x, y], 3, "b")
print "Polynomials B_x and B_y:"
pprint(B_x)
pprint(B_y)

print "divergence:"
div = B_x.diff(x) + B_y.diff(y)
pprint(div)
print "we put it equal to zero, this yields the following 6 constrains:"
constrains = [
    div.subs({x: 0, y: 0}),
    div.coeff(x).subs({y:0}),
    div.coeff(y).subs({x:0}),
    div.coeff(x*y),
    div.coeff(x**2),
    div.coeff(y**2)
]
pprint(constrains)

print "integrals:"
var("h_x h_y")
integrals = [
    integrate_line(B_x, [-h_x/2, 0], [-h_x/2, h_y]),
    integrate_line(B_x, [-h_x/2, -h_y], [-h_x/2, 0]),

    integrate_line(B_x, [0, -3*h_y/2], [0, -h_y/2]),
    integrate_line(B_x, [0, -h_y/2], [0, h_y/2]),
    integrate_line(B_x, [0, h_y/2], [0, 3*h_y/2]),

    integrate_line(B_x, [h_x/2, 0], [h_x/2, h_y]),
    integrate_line(B_x, [h_x/2, -h_y], [h_x/2, 0]),


    integrate_line(B_y, [-h_x, h_y/2], [0, h_y/2]),
    integrate_line(B_y, [0, h_y/2], [h_x, h_y/2]),

    integrate_line(B_y, [-3*h_x/2, 0], [-h_x/2, 0]),
    integrate_line(B_y, [-h_x/2, 0], [h_x/2, 0]),
    integrate_line(B_y, [h_x/2, 0], [3*h_x/2, 0]),

    integrate_line(B_y, [-h_x, -h_y/2], [0, -h_y/2]),
    integrate_line(B_y, [0, -h_y/2], [h_x, -h_y/2]),
]
pprint(integrals)
