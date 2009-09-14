from sympy.physics.qft import (wick, double_factorial, graph2nx, is_connected,
        filter_connected, graph_plot, graph2fields)

print "wick"
all = wick({1: 1, 2: 4, 3: 1, 4: 4})
print "connected"
connected = filter_connected(all)
print "-"*80
print len(all), len(connected)
for i in range(len(all)):
    g = all[i]
    print g
    f = graph_plot(g)
    f.gca().set_title(str(g))
    f.savefig("/tmp/a%04d.png" % i)
