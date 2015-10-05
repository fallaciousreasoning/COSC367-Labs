from search import *


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty list."""
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        while len(self.container) > 0:
            yield self.container.pop()


class OrderedExplicitGraph(ExplicitGraph):
    def __init__(self, nodes, edges, starting_list, goal_nodes, estimates=None):
        assert all(tail in nodes and head in nodes for tail, head, *_ in edges) \
            , "edges must link two existing nodes!"
        assert all(node in nodes for node in starting_list), \
            "The starting_states must be in nodes."
        assert all(node in nodes for node in goal_nodes), \
            "The goal states must be in nodes."

        self.nodes = nodes
        edges = sorted(edges, key=lambda edge: edge[1], reverse=True)
        edges.sort(key=lambda edge: edge[0])
        self.edge_list = edges
        self.starting_list = starting_list
        self.goal_nodes = goal_nodes
        self.estimates = estimates

    def outgoing_arcs(self, node):
        for edge in self.edge_list:
            tail, head = edge[:2]
            if tail == node:
                cost = edge[2] if len(edge) > 2 else 1
                yield Arc(tail, head, str(tail) + '->' + str(head), cost)