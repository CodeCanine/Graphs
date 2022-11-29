# Practice project for graphs and their methods.
# Time and Space complexity: O(n)
# Only manual tests in this version of the project for now.
# Methods written and commented in methods.py, used here.

from methods import *

# i---j
# |
# k---m
# |
# l

# o---n
edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

#   x---y
#  /     \
# w       z
#  \     /
#   \   /
#     v
edges1 = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

# a-->c
# |  |
# v  v
# b  e
# |
# v
# d<--f
graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# f-->i-->k
# |/ /
# g j
# |
# h
# graph1 = {
#     'f': ['g', 'i'],
#     'g': ['h'],
#     'h': [],
#     'i': ['g', 'k'],
#     'j': ["i"],
#     'k': []
# }

graph1 = {
    'f': ['g', 'i'],
    'g': ['f', 'h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ["i"],
    'k': []
}

# 3 diff connected components
# 1--2
#
#    4
#    |
# 5--6--8
#    |
# 3  7
graph2 = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}

#    5
#    | \
# 1--0--8
#
#   4---2
#    \ /
#     3
graph3 = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

# 'W'ater and 'L'and finder in graph form
grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

# Graph / adjacency list
visited_list = []

if __name__ == '__main__':
    # Traversal Methods:
    print("DFS Traversal Iterative approach:")
    # * operator to unzip the returned list
    print(*dfs_traversal_iter(graph, 'a'))

    print("\nDFS Traversal Recursive approach:")
    dfs_traversal_rec(graph, visited_list, 'a')
    # No return value needed for this method, as it uses a global variable visited_list
    print(*visited_list)

    print("\nBFS Traversal Iterative approach:")
    print(*bfs_traversal_iter(graph, 'a'))

    # Path Determination Methods:
    print("\nDFS Recursive Path Determination:")
    print(has_path_dfs_rec(graph1, 'f', 'k', set()))
    print("\nDFS Iterative Path Determination:")
    print(has_path_dfs_iter(graph1, 'f', 'k'))
    print("\nBFS Iterative Path Determination:")
    print(has_path_bfs_iter(graph1, 'f', 'k'))

    print(f"\nBuild Graph from following edges: {edges}\n")
    print(build_graph(edges))

    # Connections
    print('\nConnected components:')
    print(connected_components(graph3))
    print('\nLargest component:')
    print(largest_component(graph3))
    print('\nShortest path')
    print(shortest_path(edges1, 'w', 'z'))

    # Islands
    print('\nNumber of islands:')
    print(island_count(grid))
    print("\nMinimum island size:")
    print(minimum_island_size(grid))
