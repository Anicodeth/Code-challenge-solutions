# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

      levels = defaultdict(list)
      res = []
      
      def bfs(root, dep = 0):
        if not root:
          return
        if root.left == None and root.right == None:
          levels[dep].append(root.val)
          return

        levels[dep].append(root.val)

        bfs(root.right, dep + 1)
        bfs(root.left, dep + 1)

      bfs(root)

      for level in list(levels.values()):
          res.append(sum(level)/len(level))

      return res

        



      
