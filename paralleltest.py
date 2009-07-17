from IPython.kernel import client
from sympy.utilities.runtests import run_test_function

tc = client.TaskClient()

def get_tests():
    from sympy.utilities.runtests import PyTestReporter, SymPyTests
    verbose = False
    tb = "short"
    kw = ""
    post_mortem = False
    colors = True
    r = PyTestReporter(verbose, tb, colors)
    t = SymPyTests(r, kw, post_mortem)
    t.add_paths(["sympy/"])
    tests = []
    for filename in t._tests:
        tests += t.collect_tests_in_file(filename)
    return tests

tests = get_tests()

@tc.parallel()
def run_test(num):
    r, info = run_test_function(tests[num])
    if r in ["pass", "xpass"]:
        result = (".",  None)
    elif r == "skipped":
        result = ("", None)
    elif r == "xfail":
        result = ("X", None)
    else:
        result = ("F",  info)
    return result

#print run_test(tests[0])
#print tests[:100]
#for i in tests[:10]:
 #   t = run_test(i)
  #  print i.func_name, t[0], t[1]
print run_test(range(100))
#print map(run_test_function, tests[:100])
