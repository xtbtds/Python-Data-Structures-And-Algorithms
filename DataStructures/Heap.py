"""
Implementation of MinHeap without any libraries in pure python.

Binary heap is a complete binary tree with N nodes, 
it has has smallest possible height which is log_2^N.
Each node has greater value than any of its children.
"""


class MinHeap():
    def __init__(self, capacity):
        self.INT_MIN = -2147483648
        self.size = 0
        self.capacity = capacity
        self.array = []
    def parent(self, i):
        return round((i-1)/2)

    def leftChild(self, i):
        return i*2+1

    def rightChild(self, i):
        return i*2+2
    
    def insertKey(self, k):
        if self.size == self.capacity:
            return
        self.size += 1
        i = self.size - 1
        self.array.append(k)
        while i != 0 and self.array[self.parent(i)] > self.array[i]:
            self.array[self.parent(i)], self.array[i] = self.array[i], self.array[self.parent(i)]
            i = self.parent(i)

    def decreaseKey(self, i, new_value):    #decrease a value at i to new_value
        self.array[i] = new_value
        while i != 0 and self.array[self.parent(i)] > self.array[i]:
            self.array[self.parent(i)], self.array[i] = self.array[i], self.array[self.parent(i)]
            i = self.parent(i)

    def extractMin(self):   #extract root
        if self.size <= 0:
            return
        if self.size == 1:
            self.size -= 1
            return self.array[0]
        root = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1
        self.array.pop()
        self.minHeapify(root)
        return root

    def getMin(self):
        return self.array[0]
    
    def getSize(self):
        return self.size

    def deleteKeyAt(self, i):   #delete key at i
        self.decreaseKey(i, self.INT_MIN)
        self.extractMin()

    def minHeapify(self, i):    #heapify a subtree with the root at given index (subtrees are already heapified)
        l = self.leftChild(i)
        r = self.rightChild(i)
        smallest = i
        if l < self.size:
            if self.array[l] < self.array[i]:
                smallest = l
        if r < self.size:
            if self.array[r] < self.array[smallest]:
                smallest = r
        if smallest != i:
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
            self.minHeapify(smallest)
        
if __name__ == "__main__":
    h = MinHeap(10)
    h.insertKey(0)
    h.insertKey(1)
    h.insertKey(2)
    h.insertKey(3)
    h.insertKey(4)
    h.extractMin()
    h.deleteKeyAt(2)
    print(h.array)

        











