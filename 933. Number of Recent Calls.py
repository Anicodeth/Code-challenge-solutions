class RecentCounter:

    def __init__(self):
      self.rec = deque()
        

    def ping(self, t: int) -> int:
      self.rec.append(t)

      while self.rec[0] < t - 3000:
        self.rec.popleft()

      return len(self.rec)

        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
