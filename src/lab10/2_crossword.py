__author__ = 'jayha_000'

from csp import *

crossword_puzzle = CSP(
    var_domains={
        # read across:
        'a1': "bus,has".split(','),
        'a3': "lane,year".split(','),
        'a4': "ant,car".split(','),
        # read down:
        'd1': "buys,hold".split(','),
        'd2': "search,syntax".split(','),
    },
    constraints={
        lambda a1, d1: a1[0] == d1[0],
        lambda d1, a3: d1[2] == a3[0],
        lambda a1, d2: a1[2] == d2[0],
        lambda d2, a3: d2[2] == a3[2],
        lambda d2, a4: d2[4] == a4[0],
    })

print(sorted(crossword_puzzle.var_domains['a1']))
