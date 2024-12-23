# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def countSwaps(arr):
            arr = [ (val, i) for i, val in enumerate(arr)]
            arr.sort()
            n = len(arr)
            visited = [False] * n 
            swaps = 0

            for i in range(n):
                if visited[i]: continue
                j = i
                cycles = 0

                while not visited[j]: 
                    visited[j] = True
                    cycles += 1
                    j = arr[j][1]
                swaps += (cycles - 1)
            return swaps

        dic = defaultdict(list)
        que = deque([root])
        level = 0

        while que:
            levelSize = len(que)  
            for _ in range(levelSize):
                node = que.popleft()
                if node.left : que.append(node.left)
                if node.right : que.append(node.right)
                dic[level].append(node.val)
            level += 1

        operations = 0
        for key in dic:
            operations += countSwaps(dic[key])

        return operations


            
