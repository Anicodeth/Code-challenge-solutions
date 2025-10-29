# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse(self, root):
        if not root:
            return []
        return self.traverse(root.left) + [root.val] + self.traverse(root.right) 

    def isValidBST(self, root):
        ordered = self.traverse(root)
        n = len(ordered)

        for i in range(1, n):
            if ordered[i] <= ordered[i - 1]:
                return False

        return True
