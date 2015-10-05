__author__ = 'jayha_000'

import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    Author: Kourosh Neshatian
    Last Modified: 31 Jul 2015

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = r"\s*(?P<HEAD>{ATOM})\s*".format(**locals())
    BODY   = r"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*".format(**locals())
    CLAUSE = r"{HEAD}(:-{BODY})?\.".format(**locals())
    KB     = r"^({CLAUSE})*$".format(**locals())

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


def know(proposition, things_we_know):
    for implied_by in proposition[1]:
        if implied_by not in things_we_know:
            return False

    return True


def forward_deduce(propositions):
    propositions = list(clauses(propositions))

    things_we_know = []
    i = 0
    while i < len(propositions):
        proposition = propositions[i]
        if know(proposition, things_we_know):
            things_we_know.append(propositions.pop(i)[0])
            i = 0
        else:
            i += 1


    return things_we_know


kb = """
a :- b.
b.
"""

print(", ".join(sorted(forward_deduce(kb))))

kb = """
wet :- is_raining.
wet :- sprinkler_is_going.
wet.
"""

print(len(forward_deduce(kb)))

kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

print(", ".join(sorted(forward_deduce(kb))))
