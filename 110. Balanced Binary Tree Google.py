# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(root):
            nonlocal ans

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            diff = abs(left - right)

            if diff > 1:
                ans = False

            return max(left, right) + 1

        dfs(root)

        return ans
