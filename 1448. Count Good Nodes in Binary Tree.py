# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
      count  = 0
      def dfs(root, maxi):
        nonlocal count
        if not root:
          return
        
        elif root.val >= maxi:
          count += 1

        dfs(root.left, max(maxi, root.val))
        dfs(root.right, max(maxi, root.val))
    
      dfs(root, -inf)
      return count

