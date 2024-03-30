# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0, True

            left, lt = dfs(root.left)
            right, rt = dfs(root.right)

            diff = abs(left - right)

            if diff > 1:
                return 0, False

            return max(left, right) + 1, lt and rt

        _, val = dfs(root)

        return val
