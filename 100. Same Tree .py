# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if p and q:
        if self.isSameTree(p.left,q.left) == False:
          return False
        
        elif (p.val != q.val):
          return False

        elif self.isSameTree(p.right,q.right) == False:
          return False

      elif (p and not q) or (q and not p):
        return False   
      return True


