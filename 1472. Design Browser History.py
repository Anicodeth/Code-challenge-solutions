class node:
  def __init__(self,val):
    self.val=val
    self.next=None
    self.prev=None

class BrowserHistory:

    def __init__(self, homepage: str):
      self.head=node(homepage)
      self.last=self.head

    def visit(self, url: str) -> None:
      urlnode=node(url)
      self.last.next=urlnode
      urlnode.prev=self.last
      self.last=urlnode
      
    def back(self, steps: int) -> str:
      for _ in range(steps):
        if self.last.prev == None: break
        self.last=self.last.prev
      return self.last.val


    def forward(self, steps: int) -> str:
      for _ in range(steps):
        if self.last.next == None: break
        self.last=self.last.next
      return self.last.val
       
        

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
