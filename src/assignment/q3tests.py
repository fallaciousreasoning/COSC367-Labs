from assignment.Assignment import *

import time

start = time.clock()

# All of these should execute in less than 5 seconds,
# mine does it in 0.133 secs

map_str = """\
+-------------+
|             |
|  X          |
|  X S        |
|  XXXXXX     |
| G           |
+-------------+
"""

map_graph = MapGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +-------------+
# |  *...       |
# | *X*..       |
# |.*X.S.       |
# |.*XXXXXX     |
# | G           |
# +-------------+

map_str = """\
+-------------+
|             |
|  X          |
|  X S        |
|  XXXXXX     |
| G           |
+-------------+
"""

map_graph = MapGraph(map_str)
frontier = LCFSFrontier()
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +-------------+
# |..*........  |
# |.*X*.......  |
# |.*X.S......  |
# |.*XXXXXX...  |
# | G.   .....  |
# +-------------+

map_str = """\
+-------------+
|             |
|             |
|     S       |
|             |
| G           |
+-------------+
"""

map_graph = MapGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +-------------+
# |             |
# |    .        |
# |   ..S       |
# |  ..*        |
# | G**         |
# +-------------+

map_str = """\
+------+
|      |
|S X   |
|XXXXX |
|G X   |
|      |
+------+
"""

map_graph = MapGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +------+
# |..**..|
# |S*X.*.|
# |XXXXX*|
# |G.X.* |
# | ***  |
# +------+

map_str = """\
+------------+
|         X  |
| S       X G|
|         X  |
|         X  |
|         X  |
+------------+
"""

map_graph = MapGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +------------+
# |.........X  |
# |.S.......X G|
# |.........X  |
# |.........X  |
# |.........X  |
# +------------+

map_str = """\
+-------------+
|         G   |
| S           |
|         S   |
+-------------+
"""

map_graph = MapGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +-------------+
# |         G   |
# | S      .*.  |
# |         S   |
# +-------------+

map_str = """\
+---------+
|         |
|    G    |
|         |
+---------+
"""

map_graph = MapGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +---------+
# |         |
# |    G    |
# |         |
# +---------+

map_str = """\
+---------------+
|    G          |
|XXXXXXXXXXXX   |
|           X   |
|  XXXXXX   X   |
|  X S  X   X   |
|  X        X   |
|  XXXXXXXXXX   |
|               |
+---------------+
"""

map_graph = MapGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +---------------+
# |    G*******   |
# |XXXXXXXXXXXX*  |
# |..******...X*. |
# |.*XXXXXX*..X*..|
# |.*X.S**X*..X*..|
# |.*X....*...X*..|
# |.*XXXXXXXXXX*..|
# |..**********...|
# +---------------+

map_str = """\
+------------+
|            |
|            |
|            |
|    S       |
|            |
|            |
| G          |
|            |
+------------+
"""

map_graph = MapGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +------------+
# |            |
# |            |
# |            |
# |    S       |
# |   *        |
# |  *         |
# | G          |
# |            |
# +------------+

map_str = """\
+------------+
|            |
|            |
|            |
|    S       |
|            |
|            |
| G          |
|            |
+------------+
"""

map_graph = MapGraph(map_str)
frontier = LCFSFrontier()
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +------------+
# |  ......    |
# |  ......    |
# |  ......    |
# |  ..S...    |
# |  .*....    |
# |  *.....    |
# | G......    |
# |            |
# +------------+

map_str = """\
+----+
|    |
| SX |
| X G|
+----+
"""

map_graph = MapGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +----+
# |    |
# | SX |
# | X*G|
# +----+

map_str = """\
+--+
|GS|
+--+
"""
map_graph = MapGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +--+
# |GS|
# +--+

map_str = """\
+-------+
|     XG|
|X XXX  |
| S     |
+-------+
"""
map_graph = MapGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Answer
# +-------+
# |     XG|
# |X XXX* |
# | S***  |
# +-------+

map_str = """\
+--------------------------+
|                          |
|                          |
|  S          G         S  |
|                          |
|                          |
+--------------------------+
"""

map_graph = MapGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = generic_search(map_graph, frontier)
print_map(map_graph, frontier, solution)

# Just note that this one tripped me up
# Answer
# +--------------------------+
# |               .......    |
# |              .........   |
# |  S          G.........S  |
# |              *.......*   |
# |               *******    |
# +--------------------------+

end = time.clock()
print("Took", end - start, "seconds")