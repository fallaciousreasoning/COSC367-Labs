__author__ = 'jayha_000'

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

if __name__ == '__main__':
    print(conflict_count((1, 2))) 	#1
    print(conflict_count((1, 3, 2))) 	#1
    print(conflict_count((1, 2, 3))) 	#3
    print(conflict_count((1,))) 	#0
    print(conflict_count((1, 2, 3, 4, 5, 6, 7, 8))) 	#28
    print(conflict_count((2, 3, 1, 4))) 	#1
