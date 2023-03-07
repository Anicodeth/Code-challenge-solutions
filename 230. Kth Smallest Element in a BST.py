# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root):
      if root: return self.traverse(root.left) + [root.val] + self.traverse(root.right)
      else: return []
      
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      return self.traverse(root)[k-1]
