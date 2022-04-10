"""
Advantages over arrays:
1) Dynamic size 
2) Ease of insertion/deletion

Drawbacks: 
1) Random access is not allowed. 
2) Extra memory space for a pointer
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   #initialize next as null

class LinkedList:
    def __init__(self):    #initialize the linked list
        self.head = None

    def print_llist(self): #function to print linked list
        a = self.head
        while a:           #while node exists
            print(a.data)
            a = a.next

if __name__=='__main__':
    list1 = LinkedList()

    #creating nodes
    list1.head = Node(1)
    second = Node(2)
    third = Node(3)

    #link from head to second
    list1.head.next = second

    #link from second to third
    second.next = third

    #print linked list
    list1.print_llist()