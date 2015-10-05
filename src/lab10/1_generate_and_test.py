__author__ = 'jayha_000'

from csp import *
import itertools

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

if __name__ == '__main__':
    simple_csp = CSP(
        var_domains={x: list(range(1, 5)) for x in 'abc'},
        constraints={
            lambda a, b: a < b,
            lambda b, c: b < c,
        })

    solutions = sorted(str(sorted(solution.items())) for solution
                       in generate_and_test(simple_csp))
    print("\n".join(solutions))