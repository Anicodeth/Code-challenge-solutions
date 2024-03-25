# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        count = defaultdict(int)

        def traverse(root):
            if not root:
                return 0

            left = traverse(root.left)
            right = traverse(root.right)

            subSum = left + right + root.val

            count[subSum] += 1

            return subSum

        traverse(root)

        maxi = max(count.values())
        res = []

        for key in count:
            if count[key] == maxi:
                res.append(key)

        return res
        
