# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
      strs = []
      def dfs(root, curr):
        if not root.left and not root.right:
           strs.append(int(curr+ str(root.val)))          
        if root.left:
          dfs(root.left, curr + str(root.val))
        if root.right:
          dfs(root.right, curr + str(root.val))

      dfs(root, "")
      return sum(strs)


    
