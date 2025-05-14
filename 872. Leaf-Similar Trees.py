# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def traverse(root, store):
            if not root:
                return
            if not root.left and not root.right:
                store.append(root.val)
                return

            traverse(root.left, store)
            traverse(root.right, store)

        seq1, seq2 = [], []
        traverse(root1, seq1)
        traverse(root2, seq2)

        if len(seq1) != len(seq2): return False
        n = len(seq1)

        for i in range(n):
            if seq1[i] != seq2[i]: return False

        return True

