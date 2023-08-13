class QueueLL:
    def __init__(self, value):
        self.items = value *[None]
        self.value = value
        self.start = -1
        self.end = -1
    
    def __str__(self):
        # Handle the case when the queue is empty
        if self.isEmpty():
            return "Queue is empty"
        
        # When the queue is not empty
        result = []
        i = self.start
        while True:
            result.append(str(self.items[i]))
            if i == self.end:
                break
            i = (i + 1) % self.value
        
        return ' '.join(result)
    
    def isFull(self):
        if ((self.end + 1) % self.value == self.start):
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.start == -1:
            return True
        else:
            return False
    
    def enQueue(self, value):
        if self.isFull():
            print("The queue is full")
        elif(self.start == -1):
            self.start = 0
            self.end = 0
            self.items[self.end] = value
        else:
            self.end = self.end + 1
            self.items[self.end] = value
    

    def deQueue(self):
        if self.isEmpty():
            print("The queue is empty")
        elif(self.start == self.end):
            temp = self.items[self.start]
            self.start = -1
            self.end = -1
            return temp
        else:
            temp = self.items[self.start]
            self.start = self.start + 1
            return temp


q = QueueLL(6)

q.enQueue(1)
q.enQueue(2)
q.enQueue(3)
q.enQueue(4)
q.enQueue(5)
q.enQueue(6)
q.enQueue(7)

print(q)

print(q.deQueue())

print(q)
