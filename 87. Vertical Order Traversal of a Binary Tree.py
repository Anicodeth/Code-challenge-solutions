# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        repo = defaultdict(list)

        def dfs(root, i, j):
            if not root:
                return

            repo[j].append((root.val, i))

            dfs(root.left, i + 1, j - 1)
            dfs(root.right, i + 1, j + 1)
        
        dfs(root, 0, 0)

        keyvalues = sorted(repo.items())
        prune = [x[1] for x in keyvalues]

        res = []

        for row in prune:
            row.sort(key = lambda x: (x[1], x[0]))
            prunedRow = [x[0] for x in row]
            res.append(prunedRow)

        return res

        
