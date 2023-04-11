class ThroneInheritance:

    def __init__(self, kingName: str):
      self.inherit = defaultdict(list)
      self.king = kingName
      self.inherit[self.king]
      self.dead = set()
      self.line = []
        
    def birth(self, parentName: str, childName: str) -> None:
      self.inherit[parentName].append(childName)

    def death(self, name: str) -> None:
      self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
      self.line = []


      def dfs(curr):
        if len(self.inherit[curr]) == 0:
          return

        for child in self.inherit[curr]:
          if child not in self.dead:
              self.line.append(child)
          dfs(child)
      if self.king not in self.dead:
        self.line.append(self.king)
      dfs(self.king)

      return self.line


        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
