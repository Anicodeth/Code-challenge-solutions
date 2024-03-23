class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.que = deque([])
        n = len(encoding)
        for i in range(0, n, 2):
            self.que.append([encoding[i], encoding[i + 1]])
        

    def next(self, n: int) -> int:

        if not self.que:
            return -1

        while n:
            if not self.que:
                return -1
            if self.que[0][0] >= n:
                self.que[0][0] -= n
                return self.que[0][1]
            else:
                top = self.que.popleft()
                n -= top[0]


