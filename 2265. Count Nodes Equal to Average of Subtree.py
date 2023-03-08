# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
      self.count = 0
    
    def inorder(self,root):
      if root: return self.inorder(root.left) + [root.val] + self.inorder(root.right)
      else: return []

    def counter(self, root):
      if root:
        items = self.inorder(root)
        average = sum(items)/len(items)
        if root.val == int(average):
            self.count += 1
        self.counter(root.left)
        self.counter(root.right)
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
      self.counter(root)
      return self.count
