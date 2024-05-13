class Solution:
    def inorder(self, root):
      if root:
        return self.inorder(root.right) + [root.val] + self.inorder(root.left)
      else: 
        return []
      
    def reverse(self, root):
      if root:
        return self.reverse(root.left) + [root.val] + self.reverse(root.right)
      else: 
        return []
      
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      left_tree = self.inorder(root.left)
      right_tree = self.reverse(root.right)

      if left_tree == right_tree:
        return True
