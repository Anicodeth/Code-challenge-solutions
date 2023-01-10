class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.currIdx = -1
        self.lastIdx = -1

    def consec(self, num: int) -> bool:
        self.currIdx += 1
        if num != self.value:
            self.lastIdx = self.currIdx
        return self.currIdx - self.lastIdx >= self.k

