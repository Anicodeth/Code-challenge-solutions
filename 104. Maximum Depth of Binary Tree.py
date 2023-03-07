# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode],dep = 0) -> int:
      dep+=1
      if root:
        return max (self.maxDepth(root.left,dep),self.maxDepth(root.right,dep)) 
      else:
        return dep-1
