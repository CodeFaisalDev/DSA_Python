class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        value = [str(x.value) for x in self.LinkedList if x.value is not None]
        return ' '.join(value)
    
    def isEmpty(self):
        if self.LinkedList.head is None and self.LinkedList.tail is None:
            return True
        else:
            return False

    def enQueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.LinkedList.head = node
            self.LinkedList.tail = node
        else:
            self.LinkedList.tail.next = node
            self.LinkedList.tail = node
    
    def deQueue(self):
        if self.isEmpty():
            print("The queue is empty")
        else:
            tempValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            if self.LinkedList.head is None:
                self.LinkedList.tail = None
            
            return tempValue
    
    def peek(self):
        if self.isEmpty():
            print("The queue is empty")
        else:
            return self.LinkedList.head.value

    
    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None


q = Queue()

# print(q.isEmpty())

q.enQueue(1)
q.enQueue(2)
q.enQueue(3)

print(q)

print(q.deQueue())

print(q)

print(q.peek())

q.delete()

print(q)

print(q.isEmpty())
