# Vishnu Abhay Parvatikar

class Node(object):
    def __init__(self, x):
        self.data = x
        self.next = None


class Queue(object):
    def __init__(self):
        self.hnode = None
        self.tail = None

    def peek(self):
        if self.hnode is None:
            return None
        else:
            return self.hnode.data

    def enqueue(self, data):
        if self.hnode is None:
            self.hnode = Node(data)
            self.tail = self.hnode
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.hnode is None:
            return None
        else:
            ele = self.hnode.data
            nextnode = self.hnode.next
            self.hnode = nextnode
            return ele

    def print(self):
        if self.hnode is None:
            print("Empty Queue!")
        else:
            head = self.hnode
            print("Queue is : ")
            while head != None:
                print(" | ", head.data, " | ")
                head = head.next


queue = Queue()
while 1:
    ch = int(input("Enter the Choice 1)Enqueue 2)Dequeue 3)Peek 4)Print 5)Exit: "))
    if ch == 1:
        data = input("Enter Item to Push : ")
        queue.enqueue(data)
    elif ch == 2:
        data = queue.dequeue()
        if data is None:
            print("Queue is Empty !")
            continue
        print(data, " is popped.")
    elif ch == 3:
        data = queue.peek()
        print(data, " is top element")
    elif ch == 4:
        queue.print()
    elif ch == 5:
        print("Exiting!")
        break
    else:
        print("Invalid Choice")
