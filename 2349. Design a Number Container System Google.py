class NumberContainers:

    def __init__(self):
        self.indexes = defaultdict(list)
        self.container = {}

    def change(self, index: int, number: int) -> None:
        self.container[index] = number
        bisect.insort(self.indexes[number], index)

    def find(self, number: int) -> int:
        if number not in self.indexes:
            return -1
    
        for index in self.indexes[number]:
            if self.container[index] == number:
                return index

        return -1
        

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
