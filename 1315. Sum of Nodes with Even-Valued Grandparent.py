# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
      self.oddsum = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:

      def dfs(root, family ):
        if not root:
          return
        elif len(family) <=1:
          dfs(root.left, family + [root.val])
          dfs(root.right, family + [root.val])
        else:
          if family[-2] % 2 == 0:
            self.oddsum += root.val
            dfs(root.left, family + [root.val])
            dfs(root.right, family + [root.val])
          else:
            dfs(root.left, family + [root.val])
            dfs(root.right, family + [root.val])
      
      self.oddsum = 0
      dfs(root, [])
 
      return self.oddsum


