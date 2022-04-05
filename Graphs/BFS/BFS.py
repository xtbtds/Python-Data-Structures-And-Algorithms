def BFS(Graph, start_node):
    """
    INPUT PARAMS:
    Graph: dictionary where key is a node, value is a list of neighbours
    start_node: start node at the beginning of algorithm
    """
    queue = [start_node]
    visited = [False for i in range(len(Graph))]
    path = []
    while queue:
        node = queue.pop(0)
        path.append(node)
        if visited[node-1] == False:
            visited[node-1] = True
            for neighbour in Graph[node]:
                if visited[neighbour - 1] == False:
                    queue.append(neighbour)
    print(visited)
    print(path)
    """
    OUTPUT PARAMS:
    visited: boolean list, True if node was visited, False if not
    path: list of nodes in the order algorithm handles them
    """
    return visited, path


if __name__ == "__main__":
    Graph = {
        1: [2,3,4],
        2: [1,5],
        3: [4,5],
        4: [1],
        5: [2,1]
    }
    Graph = {1:[2,3], 2:[1,4], 3:[1,4],4:[]}
    start_node = 1
    BFS(Graph, start_node)

