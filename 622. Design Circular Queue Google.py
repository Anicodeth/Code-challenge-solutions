class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.que = [0 for _ in range(k)]
        self.front = 0
        self.rear = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False

        self.que[self.rear] = value
        self.rear = (self.rear + 1) % (self.size)
        self.count += 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.que[self.front] = 0
        self.front = (self.front + 1) % (self.size)
        self.count -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.que[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.que[self.rear - 1]
        

    def isEmpty(self) -> bool:
        if self.count == 0: return True
        return False
        

    def isFull(self) -> bool:
        if self.count == self.size:
            return True

        return False

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
