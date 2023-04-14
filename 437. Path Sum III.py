# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

      self.count = 0 


      def diverge(root, curr):

        if not root:
          return
        
        curr += root.val
        if curr == targetSum:
          self.count += 1

        diverge( root.left , curr )
        diverge( root.right , curr )

      def dfs(root):

        if not root:
          return

        diverge(root, 0)
        dfs(root.left)
        dfs(root.right)

      dfs(root)
      return self.count

        
