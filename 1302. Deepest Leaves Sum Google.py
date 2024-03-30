# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return (0, 0)

            if not root.right and not root.left:
                return (root.val, 1)

            leftSum, leftDepth = dfs(root.left)
            rightSum, rightDepth = dfs(root.right)

            if leftDepth > rightDepth:
                return leftSum, leftDepth + 1
            elif rightDepth > leftDepth:
                return rightSum, rightDepth + 1
            else:
                return ( leftSum + rightSum), leftDepth + 1

        return dfs(root)[0]
