__author__ = 'Jay Harris'

from search import *
import heapq
import math


class MapGraph(Graph):
    """A graph that parses a map string and determines start, goals and obstacles"""
    def __init__(self, map_str):
        """Initializes the map"""
        self.sort_order = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        self.visited = []

        map_str = map_str.strip()
        map = []
        for line in map_str.split('\n'):
            map.append(list(line.strip()))
        self.map = map

        self.start = []
        self.nodes = []
        self.edges = []
        self.goal_node = None

        self.get_nodes(map)
        pass

    def get_nodes(self, map):
        """Gets the nodes for the map"""
        for y in range(len(map)):
            for x in range(len(map[y])):
                node = (y, x)
                c = map[y][x]

                if not c in ["S", "G", "X", " "]: continue
                self.nodes.append(node)

                if c == 'S':
                    self.start.append(node)
                elif c == 'G':
                    self.goal_node = node

                self.add_edges(node, map)

    def add_edges(self, node, map):
        """Adds the edges for a node"""
        curry, currx = node
        # if the current node is a wall, it has no edges
        if map[curry][currx] == 'X': return

        for i in range(-1, 2):
            for j in range(-1, 2):
                # if we're looking at ourself, continue
                if i == j == 0: continue

                x, y = j + currx, i + curry
                # If the node is an X, don't add an edge
                if x < 0 or y < 0 or y >= len(map) or x >= len(map[y]) or map[y][x] not in ['G', 'S', ' ']: continue

                edge = ((curry, currx), (y, x), 1)
                # If we don't already have the edge, add it
                if edge not in self.edges:
                    self.edges.append(edge)

    def is_goal(self, node):
        """Determines if the specified node is the goal node"""
        return node == self.goal_node

    def starting_nodes(self):
        """Gets the starting node for the graph"""
        for node in self.start:
            yield node

    def outgoing_arcs(self, tail_node):
        """Gets the outgoing arcs for a node"""
        if tail_node in self.visited: return []

        arcs = []
        for edge in self.edges:
            tail, head = edge[:2]
            if tail == tail_node:
                cost = edge[2] if len(edge) > 2 else 1
                arcs.append(Arc(tail, head, self.direction(head, tail), cost))

        self.visited.append(tail_node)
        return sorted(arcs, key=lambda arc: self.sort_order.index(arc.label))

    @staticmethod
    def direction(head, tail):
        """Return the direction from the head node to the tail node
        >>> MapGraph.direction((1, 7), (2, 7))
        'S'
        >>> MapGraph.direction((1, 7), (2, 6))
        'SW'
        """
        x = head[1] - tail[1]
        y = head[0] - tail[0]

        result = ''
        if y > 0:
            result += "S"
        elif y < 0:
            result += "N"

        if x > 0:
            result += "E"
        elif x < 0:
            result += "W"

        return result

    def estimated_cost_to_goal(self, node):
        """Gets the estimated cost to the goal node from a node"""
        y, x = abs(node[0] - self.goal_node[0]), abs(node[1] - self.goal_node[1])
        return max(x, y)


class AStarFrontier(Frontier):
    """Represents the frontier of an A* search"""
    def __init__(self, graph):
        """Initializes the frontier"""
        self.graph = graph
        self.container = []
        self.visited = []

    def add(self, path):
        """Adds a path to the frontier"""
        if path[-1].head in self.visited: return

        cost = 0
        for arc in path:
            cost += arc[3]

        cost += self.graph.estimated_cost_to_goal(path[-1][1])

        # check and see if we have any other paths with the same cost
        found = False
        for c, paths in self.container:
            if c == cost:
                found = True
                paths.append(path)
                break

        # if not, add it to the container
        if not found:
            calculatedPath = (cost, [path])
            heapq.heappush(self.container, calculatedPath)


    def __iter__(self):
        while len(self.container) > 0:
            item = self.container[0][1]
            path = item.pop(0) if len(item) > 1 else heapq.heappop(self.container)[1][0]

            self.visited.append(path[-1].head)
            yield path


class LCFSFrontier(Frontier):
    """Represents the frontier of a Lowest Cost First Search"""
    def __init__(self):
        """Initializes the frontier"""
        self.container = []
        self.visited = []

    def add(self, path):
        """Adds a path to the frontier"""
        cost = 0
        for arc in path:
            cost += arc[3]

        found = False
        for c, paths in self.container:
            if c == cost:
                found = True
                paths.append(path)
                break

        if not found:
            calculatedPath = (cost, [path])
            heapq.heappush(self.container, calculatedPath)

    def __iter__(self):
        while len(self.container) > 0:
            item = self.container[0][1]
            path = item.pop(0) if len(item) > 1 else heapq.heappop(self.container)[1][0]

            self.visited.append(path[-1].head)
            yield path


def print_map(graph, frontier, solution):
    """Prints MapGraph and the solution"""
    map = graph.map

    if not solution is None:
        for arc in solution:
            y, x = arc.head
            if map[y][x] == ' ':
                map[y][x] = "*"

    for y, x in frontier.visited:
        if map[y][x] == ' ':
            map[y][x] = "."

    for y in range(len(map)):
        line = ""
        for x in range(len(map[y])):
            line += map[y][x]

        print(line)
