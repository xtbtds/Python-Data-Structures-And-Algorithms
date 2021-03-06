"""
Advantages over arrays:
1) Dynamic size 
2) Ease of insertion/deletion

Drawbacks: 
1) Random access is not allowed. 
2) Extra memory space for a pointer
"""

from importlib_metadata import NullFinder


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
    def delete(self, key):
        temp = self.head
        if temp == None:            #if empty
            return
        if temp.data == key:        #if delete head
            self.head = temp.next
            return
        while temp:                 #find previous
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:            #if there is no such element
            return
        prev.next = temp.next       #change the link to next


    def delete_by_position(self, position=0):
        temp = self.head
        if temp == None:            #if empty
            return
        if position == 0:           #if position is head
            self.head = temp.next
            return
        curr_pos = 0
        while curr_pos < position and temp:
            prev = temp
            temp = temp.next
            curr_pos += 1
        if curr_pos == position:    #what element is deleted
            print(f"Deleted element: {temp.data}")
        if temp == None:            #if position > len
            print(f"Given position is bigger than length of linked list. Enter position <= {curr_pos-1}")
            return
        prev.next = temp.next

#____________________REVERSE______________________
    def reverse(self):
        prev = None
        current = self.head
        while (current):
            next = current.next   #store next
            current.next = prev   #actual reversing
            prev = current        #step
            current = next
        self.head = prev
        return self




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

    list1.delete(6)
    list1.delete_by_position(3)
    list1.delete_by_position(33)

    #print linked list
    #list1.print_llist()

    list1 = list1.reverse()

    #print linked list
    list1.print_llist()

    




