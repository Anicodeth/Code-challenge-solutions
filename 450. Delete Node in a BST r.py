# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findmin(self,root):
      current = root
      while (current.left):
        current = current.left
      return current

    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
      if not root:
        return root
      if root.val > key:
        root.left = self.deleteNode(root.left,key)
      elif root.val < key:
        root.right = self.deleteNode(root.right,key)
      else:
        if not root.right:
          return root.left
        elif not root.left:
          return root.right
        
        temp = self.findmin(root.right)
        root.val = temp.val
        root.right = self.deleteNode(root.right, temp.val)

      return root
