from sympy import pi, S, sqrt, sympify, var, exp, I, sin, cos, simplify

def factorial(n):
    if n < 0:
        raise ValueError("n < 0")
    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)

def binom(a, b):
    return factorial(a) / (factorial(a-b)*factorial(b))

def wigner_d(j, m, mp, beta):
    j = sympify(j)
    m = sympify(m)
    mp = sympify(mp)
    beta = sympify(beta)
    r = 0
    if beta == pi/2:
        # Equation (5) in section 4.16, page 113, we set alpha=gamma=0 in
        # there. This equation seems to be correct.
        for k in range(2*j+1):
            if k > j+mp or k > j-m or k < mp-m:
                continue
            assert j+mp >= k
            assert k >= 0
            assert j-mp >= k+m-mp
            assert k + m - mp >= 0
            r += (-S(1))**k * binom(j+mp, k) * binom(j-mp, k+m-mp)
        r *= (-S(1))**(m-mp) * 1/2**j * sqrt(factorial(j+m) * \
                factorial(j-m) / (factorial(j+mp) * factorial(j-mp)))
    else:
        # Equation (10), section 4.16. This equation however, seems to be
        # incorrect in Varshalovich. I double checked by hand as well, and it
        # is not consistent with other equations. The correct equation
        # seems to be eq. (5), section 4.7.2, page 87, where we set
        # beta1=beta2=pi/2, and we get alpha=gamma=pi/2 and beta=phi+pi, then
        # we use the eq. (1), section 4.4. page 79, to simplify:
        # d(j, m, mp, beta+pi) = (-1)**(j-mp) * d(j, m, -mp, beta)
        # this is implemented below. It happens to be almost the same as in eq
        # (10), section 4.16, except that we need to substitute -mp for mp.
        for k in ang_range(j):
            r += wigner_d(j, m, k, pi/2) * (cos(-k*beta)+I*sin(-k*beta)) * \
                wigner_d(j, k, -mp, pi/2)
        # Then we need to fix the normalization. Unfortunately, this doesn't seem to be
        # the simplification from the equation, I found this by trial and
        # error, but maybe it can be simplified (don't forget that m, mp and j
        # can be integers or half integers):
        r = r * I**(2*j-m-mp) * (-1)**(2*m)
        # Finally, simplify the whole expression
        r = simplify(r)
    return r

def ang_range(j):
    m = j
    while m >= -j:
        yield m
        m -= 1

def print_table(j, beta):
    print "M\M'",
    for mp in ang_range(j):
        print "%15s" % mp, " ",
    print
    for m in ang_range(j):
        print "%4s" % m,
        for mp in ang_range(j):
            print "%15s" % wigner_d(j, m, mp, beta), " ",
        print
    print

var("beta")

print_table(S(1)/2, pi/2)
print_table(1, pi/2)
print_table(S(3)/2, pi/2)
print_table(2, pi/2)

print_table(S(1)/2, beta)
print_table(1, beta)
print_table(S(3)/2, beta)
#print_table(2, beta)
