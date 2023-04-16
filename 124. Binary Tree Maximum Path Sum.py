# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      self.maxs = set()

      def diverge(root):

        if not root.right and not root.left:
          self.maxs.add(root.val)
          return root.val 
        left = right = -inf     
        if root.left:
          left = diverge( root.left )
        if root.right:
          right = diverge( root.right)
        best=max(root.val, max(left , right)  + root.val)
        self.maxs.add(max(best, left + right + root.val))
        

        return best
      maxi = diverge(root)

      return max(maxi, max(self.maxs) if self.maxs else maxi)
