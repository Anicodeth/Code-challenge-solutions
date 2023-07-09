# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode],dep = 0) -> int:
      if not root: return 0
      que = deque([(root, 1)])

      while que:
        node, dep = que.popleft()

        leftchild = node.left
        rightchild = node.right

        if not leftchild and not rightchild:
          return dep

        if leftchild: que.append((leftchild, dep + 1))
        if rightchild: que.append((rightchild, dep + 1))

      return dep
