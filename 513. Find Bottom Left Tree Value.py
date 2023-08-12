class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = deque([(root, 0)])
        levels = defaultdict(list)

        while que:
            node, level = que.popleft()
            
            if node:
                levels[level].append(node.val)
                que.append((node.left, level + 1))
                que.append((node.right, level + 1))

        maxLevel = max(levels.keys())
        return levels[maxLevel][0]
