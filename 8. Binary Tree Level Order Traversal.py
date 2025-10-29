# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        dic = defaultdict(list)

        def build(root, dep, dic):
            if not root:
                return
            
            dic[dep].append(root.val)

            build(root.left, dep + 1, dic)
            build(root.right, dep + 1, dic)


        build(root, 0, dic)
        res = []
        for key in dic:
            res.append(dic[key])
        return res
            
    
        
