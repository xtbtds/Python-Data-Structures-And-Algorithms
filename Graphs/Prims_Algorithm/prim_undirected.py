# ONLY FOR GRAPH REPRESENTED AS DICT
# Finds Minimum Spanning Tree (MST) for an UNdirected graph.

import sys

def min_value_vertice(key_values, mstSet):
    min = sys.maxsize
    l = len(key_values)
    for i in range(l):
        if key_values[i] <= min and mstSet[i] == False:
            min = key_values[i]
            min_index = i+1
    return min_index
    

def prim(Graph):
    len_graph = len(Graph)
    mstSet = [False for i in range(len_graph)]
    edge_to = [None for i in range(len_graph)]
    key_values = [sys.maxsize for i in range(len_graph)]
    key_values[0] = 0
    while mstSet.count(False):
        u = min_value_vertice(key_values, mstSet)
        mstSet[u-1] =True
        for adjacent in Graph[u]:
            if Graph[u][adjacent] < key_values[adjacent-1]:
                key_values[u-1] = Graph[u][adjacent]
                edge_to[u-1] = adjacent
    return key_values, edge_to



if __name__ == "__main__":
    Graph = {
        1: {2:50, 3:45, 4:10},
        2: {1:50, 3:10, 4:15, 5:20},
        3: {5:35, 2:10, 1:45},
        4: {1:10, 2:15, 5:15},
        5: {2:20, 3:35, 4:15, 6:3},
        6: {5:3}
    }

    res, edge_to = prim(Graph)
    vertices_count = len(res)
    for i in range(vertices_count):
        if edge_to[i]:
            print(f"Edge {i+1}---{edge_to[i]}:  {res[i]}")


