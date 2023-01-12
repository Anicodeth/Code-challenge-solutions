class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnt = Counter()
        ans = 0
        for d in deliciousness:
            for i in range(22):
                ans += cnt[(1 << i) - d]
            cnt[d] += 1    
        return ans % (10 ** 9 + 7)    
