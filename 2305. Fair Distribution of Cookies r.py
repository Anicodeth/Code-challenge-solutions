class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        def dfs(i, mx):
            if mx >= self.ans:
                return
            if i == len(cookies):
                self.ans = min(self.ans, mx)
                return
            for j in range(k):
                kids[j] += cookies[i]
                dfs(i + 1, max(mx, kids[j]))
                kids[j] -= cookies[i]
            return

        kids, self.ans = defaultdict(int), inf
        cookies.sort(reverse=True)
        dfs(0,0)

        return self.ans
