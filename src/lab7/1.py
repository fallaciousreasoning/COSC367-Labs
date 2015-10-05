__author__ = 'jayha_000'

def min_value(tree):
    if not isinstance(tree, list):
        return tree

    bestValue = float("inf")
    for node in tree:
        currentValue = max_value(node)
        if currentValue < bestValue:
            bestValue = currentValue

    return bestValue

def max_value(tree):
    if not isinstance(tree, list):
        return tree

    bestValue = float("-inf")
    for node in tree:
        currentValue = min_value(node)
        if currentValue > bestValue:
            bestValue = currentValue

    return bestValue


tree = 3
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

# 3

tree = [1, 2, 3]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

#  1
#1 2 3

tree = [1, 2, [3]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

tree = [[1, 2], [3]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

tree = [[1, 2], [3, 4]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

tree = [[2, 3, 4], [1, 100, -100]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

# From the lecture notes
tree = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

tree = [[[3, 12], 8], [2, [4, 6]], [14, 5, 2]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))

tree = [[1, 4], [3, 5], [2]]
print("Game tree:", tree)
print("Root utility for maximiser:", max_value(tree))
print("Root utility for minimiser:", min_value(tree))