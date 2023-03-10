# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
      paths = []
      def path_to_leaf(root, currpath=''):
        if not root:
          return 0
        if not root.left and not root.right:
          paths.append(currpath + str(root.val))
        else:
          path_to_leaf(root.left,currpath + str(root.val) + "->" )
          path_to_leaf(root.right,currpath + str(root.val) + "->" )

      path_to_leaf(root)
      return paths




        
