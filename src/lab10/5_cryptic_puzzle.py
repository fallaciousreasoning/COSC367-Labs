__author__ = 'jayha_000'

import itertools, copy
from csp import *

def generate_and_test(csp):
    results = []
    assignments = [dict(zip(csp.var_domains.keys(),items)) for items in itertools.product(*csp.var_domains.values())]

    for assignment in assignments:
        passing = True
        for constraint in csp.constraints:
            if not satisfies(assignment, constraint):
                passing = False
                break
        if passing:
            results.append(assignment)
    return results

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    tda = {(x, c) for c in csp.constraints for x in scope(c)}
    while tda:
        x, c = tda.pop()
        ys = list(scope(c) - {x})
        new_domain = []
        for xval in csp.var_domains[x]:
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):
                    new_domain.append(xval)
                    break
        if csp.var_domains[x] != new_domain:
            csp.var_domains[x] = new_domain
            for cprime in set(csp.constraints) - {c}:
                if x in scope(c):
                    for z in scope(cprime):
                        if x != z:
                            tda.add((z, cprime))
    return csp

cryptic_puzzle = CSP(
    var_domains={x: list(range(0 if x != 'f' else 1, 10)) for x in 'twofur'},
    constraints={

        lambda t, w, o, f, u, r: len([t,w,o,f,u,r]) == len(set([t,w,o,f,u,r])),
        lambda o, r: (o + o) % 10 == r,
        lambda o, w, u: ((0 if o < 5 else 1) + w + w) % 10 == u,
        lambda w, t, o: ((0 if w < 5 else 1) + t + t) % 10 == o,
        lambda t: t + t >= 10,
        lambda f: f == 1,
    })

print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twour"))

new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['r']))

new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['w']))

new_csp = arc_consistent(cryptic_puzzle)
solutions = []
for solution in generate_and_test(new_csp):
    solutions.append(sorted((x, v) for x, v in solution.items()
                            if x in "twofur"))
print(len(solutions))
solutions.sort()
print(solutions[0])
print(solutions[5])
print([('f', 1), ('o', 4), ('r', 8), ('t', 7), ('u', 6), ('w', 3)] in solutions)
print([('f', 1), ('o', 8), ('r', 6), ('t', 9), ('u', 5), ('w', 2)] in solutions)