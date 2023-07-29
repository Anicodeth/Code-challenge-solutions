# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

      def inorder(root):
        if root:
          return inorder(root.left) + [root.val] + inorder(root.right)
        else:
          return []

      ordered = inorder(root)

      start = 0
      end = 0

      for i, num in enumerate(ordered):
        if num == low:
          start = i
        elif num == high:
          end = i

      return sum(ordered[start: end + 1])



