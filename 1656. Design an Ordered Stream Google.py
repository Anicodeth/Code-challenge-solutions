class OrderedStream:

    def __init__(self, n: int):
        self.stream = {}
        self.pointer = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []
        self.stream[idKey] = value

        while self.pointer in self.stream:
            res.append(self.stream[self.pointer])
            self.pointer += 1
        return res



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
