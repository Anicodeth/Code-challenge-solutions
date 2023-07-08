class ProductOfNumbers:

    def __init__(self):
      self.pro = [1]
        

    def add(self, num: int) -> None:
      if num == 0:
        self.pro = [1]
      else:
        self.pro.append(num * self.pro[-1])
        

    def getProduct(self, k: int) -> int:
      if k >= len(self.pro): return 0
      return self.pro[-1] // self.pro[-k-1] 
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
