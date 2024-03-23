# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return (0, 0)

            left = dfs(root.left)
            right = dfs(root.right)

            sumi = left[0] + right[0] + root.val
            numVal = right[1] + left[1] + 1
            avg = sumi // numVal

            if avg == root.val:
                res += 1

            return (sumi, numVal)

        dfs(root)

        return res

        
