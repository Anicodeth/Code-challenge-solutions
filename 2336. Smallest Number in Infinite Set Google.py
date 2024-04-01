class SmallestInfiniteSet:

    def __init__(self):
        self.removed = set()
        self.pointer = 1
        
    def popSmallest(self) -> int:
        
        while True:
            if self.pointer not in self.removed:
                val = self.pointer
                self.pointer += 1
                self.removed.add(val)
                return val
            else: 
                self.pointer += 1            
        

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
        self.pointer = min(self.pointer, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
