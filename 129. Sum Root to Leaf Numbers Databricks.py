# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []

        def recure(root, curr):
            if not root:
                return
            if not root.left and not root.right:
                res.append(int(curr + str(root.val)))
                return

            recure(root.right, curr + str(root.val))
            recure(root.left, curr + str(root.val))

        recure(root, "")

        return sum(res)
        
