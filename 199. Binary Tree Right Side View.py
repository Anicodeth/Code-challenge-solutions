# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
      self.dic = defaultdict(list)

    def levellist(self, root, dep = 0):
      if root:
        self.dic[dep].append(root.val)
        dep +=1
        self.levellist(root.left,dep)
        self.levellist(root.right,dep)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
      self.levellist(root)
      tree = list(self.dic.values())
      view = []
      print(tree)
      for level in tree:
        view.append(level[-1])
      
      return view
