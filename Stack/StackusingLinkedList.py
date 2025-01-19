class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):

        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    # Remove element that is the current head (start of the stack)
    def pop(self):

        if self.isempty():
            return None

        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    # Returns the head node data
    def peek(self):

        if self.isempty():
            return None

        else:
            return self.head.data

    # Prints out the stack
    def display(self):

        iternode = self.head
        if self.isempty():
            print("Stack Underflow")
        else:
            while(iternode != None):
                print(iternode.data, end="")
                iternode = iternode.next
                if(iternode != None):
                    print(" -> ", end="")
            return


# Creating a stack
stack = Stack()

# Pushing elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Displaying the stack
stack.display()

# Peeking at the top element
print("\nTop element:", stack.peek())

# Popping elements from the stack
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())

# Displaying the updated stack
stack.display()