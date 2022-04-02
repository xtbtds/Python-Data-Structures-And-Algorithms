#The result (connected/not connected) depends on what node we set as "start node", therefore 
    #the algorithm works correctly both with directed and undirected graphs.
#This algorithm shows if the paths from "start node" to others exist. 
#If there is at least one node path to which doesn't exist, the graph is considered to be not connected.

def DFS(Graph, current_node, visited):
    """
    Graph: dictionary where key is a node, value is a list of neighbours
    current_node: current node, start node at the beginning of algorithm
    visited: a list of visited nodes, is updated at any step of the recursion
    """
    if visited[current_node - 1]:
        return
    visited[current_node - 1] = True
    for neighbour in Graph[current_node]:
        DFS(Graph, neighbour, visited)

if __name__ == "__main__":
    Graph = {
        1: [3], 
        2: [3, 4], 
        3: [2], 
        4: [2, 5], 
        5: [4],
        6: [1]
    }
    visited = [False for i in range(len(Graph))]
    node = 3
    DFS(Graph, node, visited)

    IsConnected = 1
    for i in visited:
        if i == False:
            IsConnected = 0
            print ("The graph is NOT connected!")
            break
    if IsConnected:
        print ("The graph is connected!")
