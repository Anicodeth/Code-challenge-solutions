
class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        m = (len(self.queue) // 2)
        self.queue.insert(m, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if not self.queue: return -1
        return self.queue.pop(0)

    def popMiddle(self) -> int:
        if not self.queue: return -1
        if len(self.queue) % 2 == 0:
            return self.queue.pop((len(self.queue) // 2) -1)
        return self.queue.pop(len(self.queue) // 2)    

    def popBack(self) -> int:
        if not self.queue: return -1
        return self.queue.pop()

        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
