# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        ans = 0
        
        def inorderReversed(root):
            nonlocal ans
            if not root:
                return 0

            inorderReversed(root.right)
            ans += root.val
            root.val = ans
            inorderReversed(root.left)


        inorderReversed(root)

        return root
