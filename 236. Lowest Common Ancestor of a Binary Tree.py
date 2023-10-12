# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, key, visited):
            if not root:
                return False
            elif key == root.val:
                visited.append(root)
                return visited
            visited.append(root)
            left = dfs(root.left, key, visited)
            if left: return left
            right = dfs(root.right, key, visited)
            if right: return right
            visited.pop()

        first = dfs(root, p.val, [])
        second = set([n.val for n in dfs(root, q.val, [])])

        while first:
            can = first.pop()
            if can.val in second:
                return can

            

            
