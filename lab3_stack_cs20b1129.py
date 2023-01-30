# Vishnu Abhay Parvatikar


class Node(object):
    def __init__(self, x):
        self.data = x
        self.next = None


class Stack(object):
    def __init__(self):
        self.hnode = None

    def peek(self):
        if self.hnode is None:
            return None
        else:
            return self.hnode.data

    def push(self, data):
        if self.hnode is None:
            self.hnode = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.hnode
            self.hnode = new_node

    def pop(self):
        if self.hnode is None:
            return None
        else:
            ele = self.hnode.data
            nextnode = self.hnode.next
            self.hnode = nextnode
            return ele

    def print(self):
        if self.hnode is None:
            print("Empty Stack!")
        else:
            head = self.hnode
            print("Stack is : ")
            while head != None:
                print(" | ", head.data, " | ")
                head = head.next


stack = Stack()
while 1:
    ch = int(input("Enter the Choice 1)Push 2)Pop 3)Peek 4)Print 5)Exit: "))
    if ch == 1:
        data = input("Enter Item to Push : ")
        stack.push(data)
    elif ch == 2:
        data = stack.pop()
        if data is None:
            print("Stack is Empty !")
            continue
        print(data, " is popped.")
    elif ch == 3:
        data = stack.peek()
        print(data, " is top element")
    elif ch == 4:
        stack.print()
    elif ch == 5:
        print("Exiting!")
        break
    else:
        print("Invalid Choice")
