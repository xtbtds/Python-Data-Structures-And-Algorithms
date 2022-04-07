# ONLY FOR GRAPH REPRESENTED AS DICT

import sys
def min_distance_node(distance, sptSet):
    min = sys.maxsize
    leng = len(distance)
    for i in range(leng):
        if distance[i] < min and sptSet[i] == False:
            min = distance[i]
            min_index = i
    return min_index+1
    

def dijkstra(Graph, start_node):   #O(|V|^2)
    """
    sptset - set of vertices we had already found minimal path to
    distance - list of distances from start_node to others
    function min_distance_node - returns node which has minimum distance value in distance list
    """
    length = len(Graph)
    sptSet = [False for i in range(length)]
    distance = [sys.maxsize for i in range(length)]
    distance[start_node - 1] = 0
    for i in range(len(Graph)-1):  #O(|V|)
        u = min_distance_node(distance, sptSet)   #O(|V|)
        print(distance,sptSet,u)
        for neighbour in [key for key in Graph[u]]:  #O(|V|)
            if distance[u-1] + Graph[u][neighbour] < distance[neighbour-1]:
                distance[neighbour-1] = distance[u-1] + Graph[u][neighbour]
        sptSet[u-1] = True
    return distance

Graph = {
    1: {2:2, 3:4},
    2: {3:1, 4:7},
    3: {5:3},
    4: {6:1},
    5: {4:2, 6:5},
    6: {}
}
Graph = {
    1: {2:50, 3:45, 4:10},
    2: {3:10, 4:15},
    3: {5:30},
    4: {5:15},
    5: {2:20, 3:35},
    6: {5:3}
}
res = dijkstra(Graph, 6)
print(res)
