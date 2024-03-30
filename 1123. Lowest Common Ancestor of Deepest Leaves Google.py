# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

        def dfs(root):
            if not root:
                return (None, 0)

            leftNode, leftDepth = dfs(root.left)
            rightNode, rightDepth = dfs(root.right)

            if rightDepth > leftDepth:
                return rightNode, rightDepth + 1
            elif leftDepth > rightDepth:
                return leftNode, leftDepth + 1
            else:
                return root, leftDepth + 1

        return dfs(root)[0]
