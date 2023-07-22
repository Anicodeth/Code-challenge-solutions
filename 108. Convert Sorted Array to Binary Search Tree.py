# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

      def build_tree( num):
          if not num:
            return None
          median = len(num) // 2

          root = TreeNode(num[median])

          root.left = build_tree(num[ :median])
          root.right = build_tree(num[median + 1:])

          return root

      return build_tree(nums)
