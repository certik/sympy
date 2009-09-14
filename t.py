from sympy.physics.qft import (wick, double_factorial, graph2nx, is_connected,
        filter_connected, graph_plot, graph2fields)

print "wick"
all = wick({1: 1, 2: 1, 3: 1, 4: 1, 5: 4, 6:4})
print "connected"
connected = filter_connected(all)
print "-"*80
print len(all), len(connected)
for i, g in enumerate(connected):
    print g
    f = graph_plot(g)
    f.gca().set_title(str(g))
    f.savefig("/tmp/a%04d.png" % i)
