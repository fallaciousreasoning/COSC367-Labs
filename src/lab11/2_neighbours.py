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
    # neighbours = []
    # for i in range(len(assignment)):
    #     for j in range(0, len(assignment)):
    #         if j == i: continue
    #
    #         neighbour = []
    #         for k in range(len(assignment)):
    #             if k == j:
    #                 neighbour.append(assignment[i])
    #             elif k == i:
    #                 neighbour.append(assignment[j])
    #             else:
    #                 neighbour.append(assignment[k])
    #         neighbours.append(tuple(neighbour))
    # return neighbours

if __name__ == "__main__":
    print(neighbours((1, 2))) 	#[(2, 1)]
    print(sorted(neighbours((1, 3, 2)))) 	#[(1, 2, 3), (2, 3, 1), (3, 1, 2)]
    print(sorted(neighbours((1, 2, 3)))) 	#[(1, 3, 2), (2, 1, 3), (3, 2, 1)]
    print(neighbours((1,))) 	#[]
    for neighbour in sorted(neighbours((1, 2, 3, 4, 5, 6, 7, 8))):
        print(neighbour)
        # (1, 2, 3, 4, 5, 6, 8, 7)
        # (1, 2, 3, 4, 5, 7, 6, 8)
        # (1, 2, 3, 4, 5, 8, 7, 6)
        # (1, 2, 3, 4, 6, 5, 7, 8)
        # (1, 2, 3, 4, 7, 6, 5, 8)
        # (1, 2, 3, 4, 8, 6, 7, 5)
        # (1, 2, 3, 5, 4, 6, 7, 8)
        # (1, 2, 3, 6, 5, 4, 7, 8)
        # (1, 2, 3, 7, 5, 6, 4, 8)
        # (1, 2, 3, 8, 5, 6, 7, 4)
        # (1, 2, 4, 3, 5, 6, 7, 8)
        # (1, 2, 5, 4, 3, 6, 7, 8)
        # (1, 2, 6, 4, 5, 3, 7, 8)
        # (1, 2, 7, 4, 5, 6, 3, 8)
        # (1, 2, 8, 4, 5, 6, 7, 3)
        # (1, 3, 2, 4, 5, 6, 7, 8)
        # (1, 4, 3, 2, 5, 6, 7, 8)
        # (1, 5, 3, 4, 2, 6, 7, 8)
        # (1, 6, 3, 4, 5, 2, 7, 8)
        # (1, 7, 3, 4, 5, 6, 2, 8)
        # (1, 8, 3, 4, 5, 6, 7, 2)
        # (2, 1, 3, 4, 5, 6, 7, 8)
        # (3, 2, 1, 4, 5, 6, 7, 8)
        # (4, 2, 3, 1, 5, 6, 7, 8)
        # (5, 2, 3, 4, 1, 6, 7, 8)
        # (6, 2, 3, 4, 5, 1, 7, 8)
        # (7, 2, 3, 4, 5, 6, 1, 8)
        # (8, 2, 3, 4, 5, 6, 7, 1)
    for neighbour in sorted(neighbours((2, 3, 1, 4))):
        print(neighbour)
        # (1, 3, 2, 4)
        # (2, 1, 3, 4)
        # (2, 3, 4, 1)
        # (2, 4, 1, 3)
        # (3, 2, 1, 4)
        # (4, 3, 1, 2)
