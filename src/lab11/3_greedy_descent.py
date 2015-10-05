__author__ = 'jayha_000'

import itertools

def neighbours(assignment):
    neighbours = []
    for change in itertools.combinations(assignment, 2):
        neighbour = list(assignment)
        a = neighbour.index(change[0])
        b = neighbour.index(change[1])

        neighbour[a] = assignment[b]
        neighbour[b] = assignment[a]
        neighbours.append(tuple(neighbour))

    return neighbours

def conflict_count(assignments):
    conflicts = 0
    for i in range(len(assignments)):
        for j in range(i + 1, len(assignments)):
            x, y = j - i,  assignments[j] - assignments[i]
            if x == 0 or y == 0: continue

            r = abs(x / y)
            if r == 1:
                conflicts += 1

    return conflicts

def greedy_descent(assignment):
    while True:
        conflicts = conflict_count(assignment)
        print("Assignment:", assignment, "Number of conflicts:", conflicts)

        if conflicts == 0:
            print("A solution is found.")
            break

        n = sorted(neighbours(assignment))
        assignment = min(n, key=lambda neighbour: conflict_count(neighbour))
        new_conflicts = conflict_count(assignment)

        if new_conflicts >= conflicts:
            print("A local minimum is reached.")
            break

if __name__ == "__main__":
    greedy_descent((1, 2, 3, 4, 5, 6))
    # Assignment: (1, 2, 3, 4, 5, 6) Number of conflicts: 15
    # Assignment: (1, 2, 3, 4, 6, 5) Number of conflicts: 7
    # Assignment: (4, 2, 3, 1, 6, 5) Number of conflicts: 3
    # Assignment: (4, 2, 3, 5, 6, 1) Number of conflicts: 2
    # Assignment: (4, 1, 3, 5, 6, 2) Number of conflicts: 1
    # A local minimum is reached.
    greedy_descent((6, 5, 3, 4, 2, 1))
    # Assignment: (6, 5, 3, 4, 2, 1) Number of conflicts: 7
    # Assignment: (2, 5, 3, 4, 6, 1) Number of conflicts: 3
    # Assignment: (2, 5, 1, 4, 6, 3) Number of conflicts: 1
    # A local minimum is reached.
    greedy_descent((2, 1, 3, 4, 6, 5))
    # Assignment: (2, 1, 3, 4, 6, 5) Number of conflicts: 5
    # Assignment: (2, 1, 5, 4, 6, 3) Number of conflicts: 3
    # Assignment: (4, 1, 5, 2, 6, 3) Number of conflicts: 0
    # A solution is found.
    # greedy_descent((1,)) 	Assignment: (1,) Number of conflicts: 0
    # A solution is found.
    greedy_descent((1, 2))
    # Assignment: (1, 2) Number of conflicts: 1
    # A local minimum is reached.
    greedy_descent(tuple(range(1, 4)))
    # Assignment: (1, 2, 3) Number of conflicts: 3
    # Assignment: (1, 3, 2) Number of conflicts: 1
    # A local minimum is reached.
    greedy_descent(tuple(range(1, 6)))
    # Assignment: (1, 2, 3, 4, 5) Number of conflicts: 10
    # Assignment: (1, 2, 3, 5, 4) Number of conflicts: 4
    # Assignment: (1, 2, 4, 5, 3) Number of conflicts: 2
    # Assignment: (1, 4, 2, 5, 3) Number of conflicts: 0
    # A solution is found.
    greedy_descent(tuple(range(1, 11)))
    # Assignment: (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) Number of conflicts: 45
    # Assignment: (1, 2, 3, 4, 5, 6, 7, 8, 10, 9) Number of conflicts: 29
    # Assignment: (1, 2, 3, 4, 8, 6, 7, 5, 10, 9) Number of conflicts: 17
    # Assignment: (1, 2, 3, 6, 8, 4, 7, 5, 10, 9) Number of conflicts: 9
    # Assignment: (1, 7, 3, 6, 8, 4, 2, 5, 10, 9) Number of conflicts: 5
    # Assignment: (1, 6, 3, 7, 8, 4, 2, 5, 10, 9) Number of conflicts: 4
    # Assignment: (1, 6, 3, 7, 8, 4, 2, 10, 5, 9) Number of conflicts: 2
    # Assignment: (1, 6, 3, 7, 2, 4, 8, 10, 5, 9) Number of conflicts: 1
    # Assignment: (1, 6, 9, 7, 2, 4, 8, 10, 5, 3) Number of conflicts: 0
    # A solution is found.
