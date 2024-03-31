# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def inorder(root, order):
            if not root:
                return
            inorder(root.left, order)
            order.append(root.val)
            inorder(root.right, order)

        def merge(left, right):
            merged = []
            n, m = len(left), len(right)
            p1 = p2 = 0

            while p1 < n and p2 < m:

                if left[p1] >= right[p2]:
                    merged.append(right[p2])
                    p2 += 1
                else:
                    merged.append(left[p1])
                    p1 += 1     

            if p1 < n:
                merged.extend(left[p1:])
            if p2 < m:   
                merged.extend(right[p2:])    

            return merged       

        list1, list2 = [], []
        inorder(root1, list1)
        inorder(root2, list2)

        return merge(list1, list2)

        
