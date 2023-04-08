"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
      self.global_max = 0
    def maxDepth(self, root: 'Node') -> int:
      if not root:
        return 0

      def dfs(root, dep):

        if dep > self.global_max:
          self.global_max = dep

        if not root.children:
          return False

        for child in root.children:
          dfs(child, dep+1)


      dfs(root,1)

      return self.global_max
