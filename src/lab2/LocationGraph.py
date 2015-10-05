__author__ = 'jayha_000'

from search import *
from math import sqrt
from heapq import *

class LocationGraph(ExplicitGraph):
    def __init__(self, nodes, locations, edges, starting_list, goal_nodes, estimates=None):
        temp_edges = set()
        for edge in edges:
            cost = self.distance(locations[edge[0]], locations[edge[1]])
            temp_edges.add((edge[0], edge[1], cost))
            temp_edges.add((edge[1], edge[0], cost))
        super(LocationGraph, self).__init__(nodes=nodes, edge_list=list(temp_edges), starting_list=starting_list,
                                            goal_nodes=goal_nodes, estimates=estimates)
        self.locations = locations

    def outgoing_arcs(self, node):
        arcs = ExplicitGraph.outgoing_arcs(self, node)
        return sorted(arcs, key=lambda arc: arc[2])

    def distance(self, point1, point2):
        xdist = point1[0] - point2[0]
        ydist = point1[1] - point2[1]
        return sqrt(xdist ** 2 + ydist ** 2)

class LCFSFrontier(Frontier):
    def __init__(self):
        self.container = []

    def add(self, path):
        cost = 0
        for arc in path:
            cost += arc[3]
        calculatedPath = (cost, path)
        heappush(self.container, calculatedPath)

    def __iter__(self):
        while len(self.container) > 0:
            yield heappop(self.container)[1]
