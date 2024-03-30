# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None

        def traverse(root):
            nonlocal ans
            if not root:
                return False

            left = traverse(root.left)
            right = traverse(root.right)

            if ((root.val in {p.val, q.val}) and left) or ((root.val in {q.val, p.val}) and right) or (left and right):
                ans = root
                return False
       
            if root.val == p.val or root.val == q.val:
                return True

            return left or right

        traverse(root)
        return ans 
