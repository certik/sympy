from sympy.physics.qft import (wick, double_factorial, graph2nx, is_connected,
        filter_connected, graph_plot)

print "wick"
all = wick({1: 1, 2: 4, 3: 1, 4: 4})
print "connected"
connected = filter_connected(all)
print "-"*80
print len(all), len(connected)
f = graph_plot(all[0])
import pylab
pylab.show()
