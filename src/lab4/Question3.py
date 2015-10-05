__author__ = 'jayha_000'

from search import *
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

class KBGraph(ExplicitGraph):
    def __init__(self, kb, query):
        self.clauses = sorted(clauses(kb), key=lambda x: len(x[1]))

        nodes = []
        edges = []
        starting_list = []

        for node, prereqs in self.clauses:
            if node not in nodes:
                nodes.append(node)

            if len(prereqs) == 0:
                starting_list.append(node)
                continue

            for prereq in prereqs:
                if prereq not in nodes:
                    nodes.append(prereq)

                edge = prereq, node
                if edge not in edges:
                    edges.append(edge)

        ExplicitGraph.__init__(self, nodes, edges, starting_list, query)


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

query = {'a'}
if generic_search(KBGraph(kb, query), BFSFrontier()):
    print("The query is true.")
else:
    print("The query is not provable.")

