# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        que = deque( [root] )
        
		# building undirected graph
        while que:
            par = que.popleft()
            
            if par.left:
                que.append(par.left)
                graph[par.val].append(par.left.val)
                graph[par.left.val].append(par.val)
            if par.right:
                que.append(par.right)
                graph[par.val].append(par.right.val)
                graph[par.right.val].append(par.val)
        
        que = deque( [target.val] )
        visited = set( [target.val] )
        while k and que:
            k -= 1
            for _ in range(len(que)):
                par = que.popleft()
                
                for child in graph[par]:
                    if child not in visited:
                        que.append(child)
                        visited.add(child)

        return list(que)
