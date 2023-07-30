class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value, location):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode
    
    def search(self, nodeValue):
        if self.head is None:
            return "Node does not exist"
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next

            return "Node does not exist"
    
    def delete(self, value):
        if self.head is None:
            print("There is no node in the list")
        
        if self.head.value == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return

        
        tempNode = self.head
        while tempNode.next is not None and tempNode.next.value != value:
            tempNode = tempNode.next

        if tempNode.next is None:
            print("Node with the given value not found")
            return

        if tempNode.next == self.tail:
            self.tail = tempNode

        tempNode.next = tempNode.next.next
    
    def deleteEntireNode(self):
        if head is None:
            print("There is no node in the list");
        else:
            self.head = None
            self.tail = None

    def display(self):
        if self.head is None:
            print("Singly Linked List does not exist")
        else:
            tempNode = self.head
            while tempNode is not None:
                print(tempNode.value, end = ", ")
                tempNode = tempNode.next


List = SinglyLinkedList()

List.insert(1, 1)
List.insert(2, 1)
List.insert(3, 1)
List.insert(4, 1)
List.insert(7, 1)
List.insert(6, 1)

List.display()  # Output: 1 2 3 4

print(List.search(4))
print(List.search(0))

List.delete(2)
List.display()
