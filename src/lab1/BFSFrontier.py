from search import *

class BFSFrontier(Frontier):
    def __init__(self):
        self.container = []

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        while len(self.container) > 0:
            yield self.container.pop(0)