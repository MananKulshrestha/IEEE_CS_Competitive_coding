class Node:
#This will be the class of each node in the doubly linked list
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
#The doubly linked list class with all the functions for the doubly linked list
    def __init__(self):
        self.head = None

    def ins_front(self, data):
    #function to insert in front of the head of the linked list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def ins_back(self, data):
    #function to insert behind the tail
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curt = self.head
        while curt.next:
            curt = curt.next
        curt.next = new_node
        new_node.prev = curt

    def traverse_forward(self):
    #traversing from the tail to the head printing all the elements
        curt = self.head
        while curt.next:
            print(curt.data, end="->")
            curt = curt.next
        print(curt.data)

    def traverse_backward(self):
    # traversing from the head to the tail printing all the elements
        if self.head is None:
            return
        curt = self.head
        while curt.next:
            curt = curt.next
        while curt.prev:
            print(curt.data, end="->")
            curt = curt.prev
        print(curt.data)



dll = DLL()
dll.ins_front(10)
dll.ins_front(5)
dll.ins_back(20)
dll.ins_back(30)

print("Forward Traversal:- ")
dll.traverse_forward()

print("Backward Traversal:-")
dll.traverse_backward()
