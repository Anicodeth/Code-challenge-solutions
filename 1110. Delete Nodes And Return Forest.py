# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        delete = set(to_delete)
        res = []

        if root and root.val not in delete:
            res.append(root)

        def forest(root, delete):
            if not root:
                return None
            else:
                root.right = forest(root.right, delete)
                root.left = forest(root.left, delete)
                if root.val in delete:
                    if root.right: res.append(root.right)
                    if root.left: res.append(root.left)
                    return None
                else:
                    return root

        forest(root, delete)
        return res

