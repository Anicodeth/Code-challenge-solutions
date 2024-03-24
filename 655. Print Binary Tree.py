# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        def calHeight(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1

            left = calHeight(root.left) + 1
            right = calHeight(root.right) + 1

            return max(left, right)

        height = calHeight(root) - 1

        matrix = [["" for _ in range((2 ** (height + 1)) - 1) ] for _ in range(height + 1)]

        def traverse(matrix, root, currRow, currCol):
            nonlocal height
            if not root:
                return
            matrix[currRow][currCol] = str(root.val)

            traverse(matrix, root.left, currRow + 1, currCol - (2**(height - currRow - 1)))
            traverse(matrix, root.right, currRow + 1, currCol + (2**(height - currRow - 1)))




        startRow = 0
        startCol = len(matrix[0]) // 2

        traverse(matrix, root, startRow, startCol)

        return matrix
        
