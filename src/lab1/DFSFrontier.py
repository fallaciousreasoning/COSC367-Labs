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