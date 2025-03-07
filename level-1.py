class Stack:  #The stack data structure's class 
    def __init__(self): #initializer of the class
        self.items = []

    def push(self, item): #function to push items to the top of the stack
        self.items.append(item)

    def pop(self): #function to pop(remove from top) from the stack
        if self.size() != 0:
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self): #function to see the top most element of the stack 
        if self.size() != 0:
            return self.items[-1]
        else:
            print("Stack is empty")

    def size(self):  #to return the size of the stack
        return len(self.items)
    
    def display(self): #functio to display the entire content of the stack
        if self.size() != 0:
            print("Stack contents:", self.items)
        else:
            print("Stack is empty")

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()
print("Peek top element:", stack.peek())

print("Popped element:", stack.pop())

print("Stack size:", stack.size())
stack.display()
