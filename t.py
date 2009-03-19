import sys

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

def run_tests(tests, nums):
    result = []
    for i in nums:
        r, info = run_test_function(tests[i])
        if r in ["pass", "xpass"]:
            result.append((".",  None))
        elif r == "skipped":
            pass
        elif r == "xfail":
            pass
        else:
            result.append(("F",  info))
    return result


from IPython.kernel import client
mec = client.MultiEngineClient()
mec.reset()
ids = mec.get_ids()
mec.push_function({
    "get_tests": get_tests,
    "run_tests": run_tests,
    })
mec.execute("tests = get_tests()")
mec.execute("ntests = len(tests)")
ntests = mec.pull("ntests")
for n in ntests:
    if n != ntests[0]:
        raise Exception("Each engine collected different tests.")
ntests = ntests[0]
print "number of tests:", ntests
mec.execute("from sympy.utilities.runtests import run_test_function")
i = 0
tasks = {}
#ntests = 20
for testi in range(ntests):
    if i not in tasks:
        tasks[i] = []
    tasks[i].append(testi)
    i += 1
    if not (i in ids):
        i = 0
    #print i, testi
mec.push(dict(tasks=tasks))
results = []
print "distributing jobs"
for target in tasks:
    pr = mec.execute("result = run_tests(tests, tasks[%d])" % target,
            targets=[target], block=False)
    results.append((target, pr))
print "collecting results"
for proc, r in results:
    print "processor:", proc
    r.get_result()
    result = mec.pull("result", targets=proc)[0]
    infos = []
    for res, info in result:
        if res == ".":
            print ".",
        else:
            print "F",
            infos.append(info)
    print "exceptions"
    for e in infos:
        print "_"*80
        print e
