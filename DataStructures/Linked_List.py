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

    #_______________________INSERT_________________________
    def push(self, new_data):     #insert in the beginning of the linked list (O(1) time)
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, new_data):     #insert after given node (O(1) time)
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):      #insert at the end (O(n) time)
        new_node = Node(new_data)
        if self.head == None:        #if linked list is empty
            self.head = new_node
            return

        last = self.head            #traverse through the linked list until we find node with next == none
        while (last.next):
            last = last.next
        last.next = new_node

    #_______________________DELETE_________________________




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

    list1.push(4)
    list1.insert_after_node(second, 5)
    list1.append(6)
    list1.insert_after_node(list1.head, 57)

    #print linked list
    list1.print_llist()



