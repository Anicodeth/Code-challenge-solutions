# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
      if root:
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
      else:
        return []
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
      values = Counter(self.inorder(root))
      sorteddict = sorted(values.items(), key= lambda item: item[1])
      mode = sorteddict[-1][1]
      res = []
      for i in range(len(sorteddict)-1,-1,-1):
        if sorteddict[i][1] != mode:
          break
        res.append(sorteddict[i][0])
      return res


