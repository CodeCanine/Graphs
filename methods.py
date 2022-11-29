# Class for method declaration, used in main.py
# Trying to implement both Depth First Search (dfs),
# and Breadth First Search (bfs) algorithms in both Iterative (iter) and Recursive (rec) form.

# Method requires a graph, and a starting position to travel through the nodes
def dfs_traversal_iter(graph, source):
    # List to store the traversed nodes
    result = []

    # DFS methods work with a stack (Last In First Out), for example
    # d -> d  -> d
    #      c
    #      b
    #      a

    # Setting root node as the first element of the stack
    stack = [source]

    while stack:
        # Examining the LAST added node to the stack, and removing it
        # ie.: stack.pop(0) would create a que instead of a stack, by removing the FIRST added node
        current = stack.pop()
        result.append(current)
        # Investigating all it's neighbours, and adding to the stack
        for neighbour in graph[current]:
            stack.append(neighbour)
    return result


# Recursive version needs a global helper "visited" list.
# No return value, as this method appends to the global visited list
# Note: Set would be more efficient, but it is UNORDERED, which would not fit this approach.
# Method needs a graph, a global visited list, and a source point in the graph to traverse through
def dfs_traversal_rec(graph, visited, source):
    # Below method examines given node and its neighbours in a stack-like manner,
    # and appends it to a global variable, calling itself until there are no more calls/elements in the graph.
    if source not in visited:
        visited.append(source)
        for neighbour in graph[source]:
            dfs_traversal_rec(graph, visited, neighbour)


# BFS Iterative approach is almost the same as DFS Iterative, only difference is it uses a QUE (FIFO)
# Instead of a STACK (LIFO) method.
# d ->
#      c
#      b
#      a -> a
def bfs_traversal_iter(graph, source):
    result = []
    que = [source]
    while que:
        current = que.pop(0)
        result.append(current)
        for neighbour in graph[current]:
            que.append(neighbour)
    return result


# Below method determines if between 2 given nodes, there is a traversable path or not recursively.
def has_path_dfs_rec(graph, source, destination, visited):
    # Exit condition
    if source == destination:
        return True
    # Precaution, if there are circles in the graph.
    if source in visited:
        return False
    visited.add(source)
    # Until there are nodes in the graph, see if it can find a path
    # if not, there are no paths
    for neighbour in graph[source]:
        if has_path_dfs_rec(graph, neighbour, destination, visited):
            return True
    return False


# Below method determines if between 2 given nodes, there is a traversable path or not iteratively.
def has_path_dfs_iter(graph, source, destination):
    # Precaution, if the source is the destination as well
    if source == destination:
        return True
    # Precaution against loops
    visited = set()
    # Data structure from which we work from
    stack = [source]
    # Until there are elements, do the following:
    while stack:
        # Analyze the current element in the stack, and remove it
        current = stack.pop()
        # Exit condition if a path can be found
        if current == destination:
            return True
        # Core, if the currently examined element is not the destination
        if current not in visited:
            # Add the element to the unique elements' set
            visited.add(current)
            # Check its neighbours
            for neighbour in graph[current]:
                stack.append(neighbour)
    # If no element left in the graph, no path can be found, return False
    return False


# BFS recursive approach could not be applied here flawlessly
# The method is very similar to BFS Iterative Traversal (and the DFS has path Iterative solution),
# only difference is, this method returns a boolean Instead of a list.
def has_path_bfs_iter(graph, source, destination):
    if source == destination:
        return True
    que = [source]
    visited = set()
    while que:
        current = que.pop(0)
        if current == destination:
            return True
        if current not in visited:
            visited.add(current)
            for neighbour in graph[current]:
                que.append(neighbour)
    return False


# From edge-pairs this method creates a graph dictionary. (Undirected)
def build_graph(edges):
    # Empty graph for the final result
    graph = {}
    # Examining all the pairs
    for edge in edges:
        # Unpacking the pairs to a,b variables
        a, b = edge
        # This creates an undirected graph, thus both a and b has to have the same neighbours
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


# This method determines, the number of separate connected components there are in the graph
def connected_components(graph):
    # Outside declaration of a helper Data Structure, that the explore function uses when it calls itself
    # So that the set does not reset with every call.
    visited_set = set()
    # Declaring a return variable with default value
    count = 0
    # Check all the nodes/neighbours in the graph
    for node in graph:
        # And if the helper function returns true,
        if explore(graph, node, visited_set) is True:
            # Raise count by 1
            count += 1
    # Return the final result
    return count


# Helper method for the connected_components method
# This is a simple recursive traversal with loop protection.
def explore(graph, current, visited_set):
    # Precaution against circles, if it already is accounted for, don't check it again
    if current in visited_set:
        return False
    visited_set.add(current)
    # Check all the neighbours, and if this returns true, return that to the connected_components method.
    for neighbour in graph[current]:
        explore(graph, neighbour, visited_set)
    return True


# Method to determine the larges connected component
def largest_component(graph):
    visited_set = set()
    longest = 0
    for node in graph:
        size = explore_size(graph, node, visited_set)
        if size > longest:
            longest = size
    return longest


# Helper method for the largest_component method
def explore_size(graph, current, visited_set):
    if current in visited_set:
        return 0
    visited_set.add(current)
    size = 1
    for neighbour in graph[current]:
        size += explore_size(graph, neighbour, visited_set)
    return size


# Method to find the shortest path between 2 given present nodes in the graph
# Just as a twist, it first builds the graph, but would work perfectly with graph instead of edges as well
def shortest_path(edges, source, destination):
    graph = build_graph(edges)
    # Precaution against loops
    visited_set = {source}
    que = [[source, 0]]
    # While there are elements in the que
    while que:
        # Split the element of the que into current and distance, and remove the current element from the que
        current, distance = que.pop(0)
        # If it is the required element, give back its distance
        if current == destination:
            return distance
        # If not, check the current, element's neighbours
        for neighbour in graph[current]:
            # Check if we have visited it before
            if neighbour not in visited_set:
                # If not, make sure we visited it (add it to the set)
                visited_set.add(neighbour)
                # and add the current element's neighbour to the que to check it as well, with 1 more distance
                que.append([neighbour, distance + 1])
    # If the element is not present, return -1, but could be anything like "not found" etc.
    return -1


def island_count(grid):
    # Set to avoid going in loops
    # Declaring outside the helper method, to avoid t resetting with every call.
    visited_set = set()
    # Counting the islands
    count = 0
    # Need to traverse the whole grid, therefore nested for loop
    for row in range(0, len(grid), 1):
        # Asymmetry grid [0]
        for col in range(0, len(grid[0]), 1):
            # If helper method found land, count it
            if explore_island(grid, row, col, visited_set) is True:
                count += 1
    return count


def print_grid(grid):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in grid]))


def explore_island(grid, row, col, visited_set):
    # Due to the nature of traversal, to avoid multiple ifs, a boundary must be given
    # To avoid fx.: (-1,0) or (4,5) coordinates, that fall outside the grid
    row_inbounds = 0 < row < len(grid)
    col_inbounds = 0 < col < len(grid[0])

    # Checking if we are still in the given grid
    if not row_inbounds or not col_inbounds:
        return False
    # Check if tile is water
    if grid[row][col] == 'W':
        return False

    # Create a tuple from the current tile's indexes, to avoid for example 0,1 and 1,0 being the same
    pos = (row, col)
    # Cycle prevention
    if pos in visited_set:
        return False
    # Add the tile to the visited set outside the method
    visited_set.add(pos)
    # Check Upwards Tile
    explore_island(grid, row - 1, col, visited_set)
    # Check Left Tile
    explore_island(grid, row + 1, col, visited_set)
    # Check Downwards Tile
    explore_island(grid, row, col - 1, visited_set)
    # Check Right Tile
    explore_island(grid, row, col + 1, visited_set)
    # If this returns True, it means it has found land, and gives this back to the main function call
    return True


# Almost the same af the island_count method, but this one compares the return value of the helper method below,
# with infinity, to determine the smallest value
def minimum_island_size(grid):
    visited_set = set()
    min_size = float('inf')
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            size = explore_island_size(grid, row, col, visited_set)
            if 1 < size < min_size:
                min_size = size
    return min_size


# Almost same as explore_island method, but this counts the return value in a variable called "size".
def explore_island_size(grid, row, col, visited_set):
    # Returns true if it is inbounds
    row_inbounds = 0 < row < len(grid)
    col_inbounds = 0 < col < len(grid[0])

    # Base case for out of bounds calls (for example 0,0)
    if not row_inbounds or not col_inbounds:
        return 0
    if grid[row][col] == 'W':
        return 0
    pos = (row, col)
    # cycle prevention
    if pos in visited_set:
        return 0
    visited_set.add(pos)

    size = 1
    size += explore_island(grid, row - 1, col, visited_set)
    size += explore_island(grid, row + 1, col, visited_set)
    size += explore_island(grid, row, col - 1, visited_set)
    size += explore_island(grid, row, col + 1, visited_set)

    return size
