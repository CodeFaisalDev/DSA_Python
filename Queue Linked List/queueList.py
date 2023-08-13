class queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        value = [str(x) for x in self.items]
        return ' '.join(value)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enQueue(self, value):
        self.items.append(value)
    
    def deQueue(self):
        if self.isEmpty():
            print("The queue is empty")
        else:
            self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            print("The queue is empty")
        else:
            return self.items[-1]

    def delete(self):
        self.items = []
    

q = queue()

q.enQueue(1)
q.enQueue(2)
q.enQueue(3)

print(q)

q.deQueue()

print(q)

print(q.peek())

q.deQueue()

print(q)
