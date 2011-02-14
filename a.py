from printing import TableForm, MatrixForm
from sympy import *
var("x y z r i n")

f = 1 + x**2 + exp(-x) + sin(2*x)
g = f + f.subs(x, y**2)
h = g + f.subs(x, z**3)
print f
print g
print h

print "Data ========================="
xdata = array([1, 2, 3, 4, 5])
ydata = xdata ** 2
data = array(zip(xdata, ydata))
data2 = array([xdata, 1.5 * ydata])
print data
print TableForm(data)
print MatrixForm(data)

print "Summation ===================="
s1 = Sum(r**i, (i, 1, n))
print s1
s2 = Sum(x**n/factorial(n), (n, 0, oo))
print s2

print "Series expansion =============="

a = 1; b = 5
s = series(f, x, a, 2)
print s

print "Derivatives ===================="
df = f.diff(x)
d2f = f.diff(x, 2)
print f
print df
print d2f

print "Integrals ======================"
i1 = integrate(f, x)
i2 = integrate(f, (x, a, b))
print i1
print i2
print N(i2)
