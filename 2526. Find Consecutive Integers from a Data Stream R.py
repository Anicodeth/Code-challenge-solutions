class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stream = []

    def consec(self, num: int) -> bool:
      self.stream.append(num)
      last = len(set(self.stream[len(self.stream)-self.k:])) if len(self.stream) >= self.k else 0

      if last == 0:
        return False
      elif last == 1 and self.stream[-1] == self.value:
        return True
      else:
        return False

        
