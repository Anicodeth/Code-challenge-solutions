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

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      tree = self.traverse(root)
      for i in range(1,len(tree)):
        if tree[i] <= tree[i-1]:
          return False
      return True
