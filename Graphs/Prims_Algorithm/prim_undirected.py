#FINDS MINIMUM SPANNING TREE (Greedy algo)

import sys

class Graph():
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)]

    def printMST(self, values, parent):
        print("edge    weight")
        for i in range(1, self.v):
            print(f"{parent[i]}-{i}     {values[i]}")

    def min_key_value(self, mstSet, values):    #select vertice with minimum values which is not in mstSet
        min = sys.maxsize
        for i in range(self.v):
            if values[i] < min and mstSet[i] == False:
                min = values[i]
                min_index = i
        return min_index

    def prim(self):
        mstSet = [False for i in range(self.v)]    #is already in MST or not
        values = [sys.maxsize for i in range(self.v)]    #minimum weights to every vertice
        values[0] = 0
        parent = [-1 for i in range(self.v)]    #list of parent vertices we pick FINAL edges with
        while mstSet.count(False):    
            u = self.min_key_value(mstSet, values)
            mstSet[u] = True
            for v in range(self.v):   #for 
                if self.graph[u][v] < values[v] and self.graph[u][v] > 0 and mstSet[v] == False:
                    values[v] = self.graph[u][v]
                    parent[v] = u
        self.printMST(values, parent)




if __name__ == "__main__":
        g = Graph(5)
        g.graph = [
                [0, 1, 8, 6, 0],
                [1, 0, 3, 8, 5],
                [8, 3, 0, 0, 7],
                [6, 8, 0, 0, 9],
                [0, 5, 7, 9, 0]
                ]
        g.prim()