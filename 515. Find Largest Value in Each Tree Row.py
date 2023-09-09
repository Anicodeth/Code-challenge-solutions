# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

      levels = defaultdict(list)

      def dfs(root, depth):
        nonlocal levels
        if not root:
          return

        levels[depth].append(root.val)
        dfs(root.left, depth + 1)
        dfs(root.right, depth + 1)

      dfs(root, 0)
      res = []
      for key in levels:
        res.append(max(levels[key]))

      return res

        
