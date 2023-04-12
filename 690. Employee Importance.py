"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def __init__(self):
      self.relations = defaultdict(list)
      self.importance = 0
    def getImportance(self, employees: List['Employee'], id: int) -> int:
      for emp in employees:
        self.relations[emp.id] = [emp.importance,emp.subordinates]
        
      def dfs(id):
        self.importance += self.relations[id][0]
        for sub in self.relations[id][1]:
          dfs(sub)

      dfs(id)

      return self.importance
        
